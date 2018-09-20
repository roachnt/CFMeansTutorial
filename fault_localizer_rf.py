import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Lasso
import pandas as pd
import numpy as np

# this function removes phi names in the ranking list


def filter_phi_rows(suspicious_df, phi_names_set):
    return suspicious_df[~suspicious_df['variable_name'].isin(phi_names_set)]

# this function appends the program result(fail or success) to each target variable's dataframe


def append_y_column(bad_dict, good_dict):

    diff_dict = {index: 0.0 if bad_dict[index] ==
                 good_dict[index] else 1.0 for index in bad_dict}
    for key in global_value_dict:
        rows = global_value_dict[key].index
        outcome_list = [diff_dict[i] for i in rows]
        global_value_dict[key]['outcome'] = outcome_list

# this function generates ranking list


def suspicious_ranking(global_value_dict, model_to_use):

    append_y_column(bad_dict, good_dict)

    suspicious_df = pd.DataFrame(
        columns=['variable_name', 'max_risk_diff', 'quantile1', 'quantile2'])
    for name in global_value_dict:
        if name in phi_names_set:
            continue
        # df cleaning
        #df = global_value_dict[name].select_dtypes(include=[np.number]).dropna(axis=1, how='all')
        df = global_value_dict[name].select_dtypes(
            include=[np.number]).dropna(axis=1, how='any')
        train_set = df
        #train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
        train_set_X = train_set.drop(['outcome'], axis=1)
        train_set_Y = train_set['outcome']
        if model_to_use == 0:
            model = RandomForestClassifier(
                n_estimators=500, max_leaf_nodes=16, n_jobs=-1)
        if model_to_use == 1:
            model = Lasso(alpha=0.1)
        model.fit(train_set_X, train_set_Y)
        W = df.iloc[:, 0].to_frame()
        quantiles = get_quantiled_tr(W)
        risk_list = predict_causal_risk_list(train_set_X, quantiles, model)
        max_risk = max(risk_list)
        min_risk = min(risk_list)
        row = [df.columns[0], max_risk - min_risk, risk_list.index(max_risk),
               risk_list.index(min_risk)]
        suspicious_df.loc[len(suspicious_df)] = row
    suspicious_df = suspicious_df.sort_values(
        by='max_risk_diff', ascending=False)
    return filter_phi_rows(suspicious_df, phi_names_set)

# this function get a list of ten traetment levels


def get_quantiled_tr(W):
    # 10 quantiles from 0.05 to 0.95
    quantile_list = []
    for i in np.arange(0.05, 1.05, 0.1):
        quantile_list.append(W.quantile(i))
    return quantile_list

# this function compute the ten counterfactual means for a treatment level


def predict_causal_risk_list(train_set_X, quantiles, model):

    risk_list = []
    # print(train_set_X.columns[0] + " being treatment...")
    X_with_quantile = train_set_X.drop(train_set_X.columns[0], axis=1)

    for quantile in quantiles:
        X_with_quantile.insert(loc=0, column=train_set_X.columns[0],
                               value=np.full((len(X_with_quantile), 1), quantile))
        # X_with_quantile[train_set_X.columns[col_index_todrop]] = np.full((len(X_with_quantile), 1), quantile)
        # print(X_with_quantile.describe())
        risk_list.append(model.predict(X_with_quantile).mean())
        X_with_quantile = X_with_quantile.drop(train_set_X.columns[0], axis=1)
    return risk_list



# correct version goes here
from MoreBuggyFcns import good_dict, bad_dict, global_value_dict, phi_names_set
# faulty version goes here
#from fib_bad import bad_dict, global_value_dict, phi_names_set
# correct version goes here
#os.system('python fib.py')
# faulty version goes here
#os.system('python fib_bad.py')
# ranking result generated by calling suspicious_ranking
# customize the second parameter: 0--> RF  1-->LASSO
result = suspicious_ranking(global_value_dict, 0)

pd.set_option("display.precision", 10)
print('*************Target variables in total: ', len(result), '*************')
print(result)

with open("result.txt", "w") as f:
    f.write(str(result))
