# ML usecases

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