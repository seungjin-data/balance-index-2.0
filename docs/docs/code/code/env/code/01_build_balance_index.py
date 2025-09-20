import pandas as pd
from pathlib import Path

RAW = Path('data/raw')
OUT = Path('data/processed')
OUT.mkdir(parents=True, exist_ok=True)

# 1) UIS 졸업자 원자료 읽기
# 기대 컬럼: iso3, year, field_code, sex, graduates
#  - field_code는 ISCED-F 2013 대분류 코드 문자열('01'~'10')
#  - sex는 M/F/Total 등 → 아래에서 합계로 집계
df = pd.read_csv(RAW / 'UNESCO_UIS.csv')

# 2) STEM/HSS 매핑
STEM = {'05', '06', '07'}
HSS  = {'01', '02', '03', '04'}

# 3) 성별 합계
d = df.groupby(['iso3', 'year', 'field_code'], as_index=False)['graduates'].sum()

# 4) 총합 및 피벗
tot = d.groupby(['iso3', 'year'])['graduates'].sum().rename('total').reset_index()
wide = d.pivot_table(index=['iso3', 'year'],
                     columns='field_code',
                     values='graduates',
                     aggfunc='sum').fillna(0)
wide = wide.merge(tot, on=['iso3', 'year'])

# 5) 비율 계산
stem_share = wide[[c for c in wide.columns if c in STEM]].sum(axis=1) / wide['total']
hss_share  = wide[[c for c in wide.columns if c in HSS ]].sum(axis=1) / wide['total']
bi = (stem_share - hss_share).abs()

# 6) 출력 저장
res = wide.reset_index()[['iso3', 'year']]
res['STEM_share'] = stem_share.values
res['HSS_share']  = hss_share.values
res['BI']         = bi.values

OUT_FN = OUT / 'balance_index_by_country_2018_2024.csv'
res.to_csv(OUT_FN, index=False)
print('Saved', OUT_FN)
