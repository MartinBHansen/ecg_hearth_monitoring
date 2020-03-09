import Physionet.DataProcessor as pdp
import Physionet.TrainingConcatPipeline as tcp

if __name__ == "__main__":
    pipeline = pdp.setup_pipeline(7500, 0.8, 0.2)

    pre_processers = []

    to_process = {
        "comp_res_loc": "/data/ltafdb.tar",
        "ext_loc": "/data/ltaf",
        "override_policy": True,
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "name":"LTAF",
        "target_label": 1,
        "sampled_frequency":128,
        "target_frequency":256
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "/data/nsrdb.tar",
        "ext_loc": "/data/nsr",
        "headders": ['sample #', 'ECG 1', 'ECG 2'],
        "override_policy": True,
        "name":"NSR",
        "target_label": 0,
        "sampled_frequency":128,
        "target_frequency":256
    }

    pre_processers.append(pipeline.execute(to_process))

    to_process = {
        "comp_res_loc": "/data/fantasia.tar",
        "ext_loc":"/data/fantasia",
        "headders": ['sample #', 'RESP', 'ECG'],
        "override_policy": True,
        "name":"Fantasia",
        "target_label": 0,
        "sampled_frequency":250,
        "target_frequency":256
    }
    pre_processers.append(pipeline.execute(to_process))

    for pre_proces_elem in pre_processers:
        pre_proces_elem.join()

    to_process = {
        "training":"/data",
        "name":"Prep training and test data",
        "concat_rate": 0.2
    }
    
    prep_train_test_data = tcp.setup_pipeline()

    prep_train_test_data.execute(to_process).join()