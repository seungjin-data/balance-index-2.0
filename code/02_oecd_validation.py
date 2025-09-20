import pandas as pd
from pathlib import Path

P = Path('data/processed')
RAW = Path('data/raw')

# 1) 균형지수 최신 연도만 추출
bi = pd.read_csv(P / 'balance_index_by_country_2018_2024.csv')  # iso3, year, STEM_share, HSS_share, BI
latest = bi.sort_values('year').groupby('iso3').tail(1)

# 2) OECD 고용률 데이터 읽기 (필수 컬럼: iso3, emp_25_34)
#    emp_25_34는 25–34세 대졸자 고용률(% 혹은 소수)
oecd = pd.read_csv(RAW / 'OECD_EAG_2024.csv')[['iso3', 'emp_25_34']]

# 3) 매칭 및 상관계수
df = latest.merge(oecd, on='iso3', how='inner').dropna(subset=['BI','emp_25_34'])
r = df['BI'].corr(df['emp_25_34'])

print('OECD 검증 표 샘플 행수:', len(df))
print('Pearson r (BI vs Employment 25–34) =', r)

# 4) 원고용 표로 저장
out = df[['iso3', 'BI', 'emp_25_34']].copy()
out.to_csv('tables/Table2_BI_vs_Employment.csv', index=False)
print('Saved tables/Table2_BI_vs_Employment.csv')
