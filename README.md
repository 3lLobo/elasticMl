# ML usecases

![image](https://github.com/3lLobo/elasticMl/assets/25290565/cfa1ab65-a7ab-4a29-a0c0-d189f0632d46)

## Anomaly detection

### Notes

- `model_plot_config` enables the threshold view, only available for single metric.
- influencers: fields which contain data which is suspected to cause anomalies.
- calendar: unusual events. Subscribed jobs will skip the time period of the event.
- [custom rules](https://www.elastic.co/guide/en/machine-learning/8.8/ml-configuring-detector-custom-rules.html): fine tune the job with exception rules.
- [api usage](https://www.elastic.co/guide/en/elasticsearch/reference/8.8/ml-ad-apis.html)


### Security jobs

Predefined jobs for security use-cases.

[Job](https://github.com/elastic/kibana/blob/8.8/x-pack/plugins/ml/server/models/data_recognizer/modules/security_linux/ml/v3_linux_anomalous_network_port_activity.json) and [detaview](https://github.com/elastic/kibana/blob/8.8/x-pack/plugins/ml/server/models/data_recognizer/modules/security_linux/ml/datafeed_v3_linux_anomalous_network_activity.json) JSONs are opensource.

Modify filed names in job and query and submit via api.


Examples:
- anomal network traffic
- unusual ports



### Advanced analytics

- job config JSON : [example](./res/job_config.json)
- datafeed JSON : [example](./res/datafeed_config.json)


### Create job via console

```bash
PUT _ml/anomaly_detectors/test-job2?pretty
```

```json
{
  "analysis_config": {
    "bucket_span": "15m",
    "detectors": [
      {
        "detector_description": "Sum of bytes",
        "function": "count"
      }
    ]
  },
  "data_description": {
    "time_field": "timestamp",
    "time_format": "epoch_ms"
  },
  "analysis_limits": {
    "model_memory_limit": "11MB"
  },
  "model_plot_config": {
    "enabled": true,
    "annotations_enabled": true
  },
  "datafeed_config":
  {
    "indices": [
    "logs-*"
    ],
    "query": {
      "bool": {
        "must": [
          {
            "match_all": {}
          }
        ]
      }
    },
    "runtime_mappings": {},
    "datafeed_id": "datafeed-test-job2"
  }
}
```


## Detectors

Detector is the function to find anomalies. Using more than one detector results in a multi-metric job. 
The basic functions such as `count` `high_count` `low_count` are based on the events field.
Functions 

Functions such as `mean` `sum` `median` `varp` require the filed to be numeric.

`distinct_count` monitors the occurrence of unique values in a field.

`rare` monitors the occurrence of rare values in a field.

Examples of functions are [here](./detectors.json).


## Datafeed

Datafeeds for jobs are determined by an existing datafeed plus a DSL query.
DSL logic is doumented [here](https://www.elastic.co/guide/en/elasticsearch/reference/8.8/query-dsl.html).
Examples for queries are [here](./dsl_queries.json).
An easy way to get a working query is to use the discover tab in kibana and then use the `edit in dsl` option to get the query.
