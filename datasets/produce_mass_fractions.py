import pandas as pd
import numpy as np

had_model = ['eposlhc', 'qgsjetII04', 'sibyll23d']

dic_eposlhc = {
    'logE' : [17.85, 17.95, 18.05, 18.15, 18.25, 18.35, 18.45, 18.55],
    'H_frac' : [.49, .57, .60, .62, .61, .51, .48, .37],
    'He_frac' : [.16, .04, .07, .07, .14, .31, .36, .47],
    'N_frac' : [.32, .39, .33, .31, .25, .18, .16, .16],
    'Fe_frac' : [.03, .0, .0, .0, .0, .0, .0, .0]
}

mass_frac_data_epos = pd.DataFrame(dic_eposlhc)

#mass_frac_data_epos['frac_sum'] = mass_frac_data_epos.apply(lambda x: x.sum() - x['logE'], axis = 1)

print(mass_frac_data_epos)

mass_frac_data_epos.to_parquet('./eposlhc/primary_mass_frac_data.parquet')
