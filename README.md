bq-results-raw-full.csv:
```
SELECT
    log_index,
    transaction_hash,
    transaction_index,
    address,
    data,
    topics[SAFE_OFFSET(0)] AS topics0,
    topics[SAFE_OFFSET(1)] AS topics1,
    topics[SAFE_OFFSET(2)] AS topics2,
    topics[SAFE_OFFSET(3)] AS topics3,
    block_timestamp,
    block_number,
    block_hash
FROM `bigquery-public-data.crypto_ethereum.logs`
WHERE 
    address IN (
        -- BTCUSD
        '0xf5fff180082d6017036b771ba883025c654bc935',
        '0x276de5c241071b4728697f4e11a377484a2dd6cb',
        '0xf570deefff684d964dc3e15e1f9414283e3f7419',
        '0x7104ac4abcecf1680f933b04c214b0c491d43ecc',
        '0xae74faa92cb67a95ebcab07358bc222e33a34da7',
        '0xdbe1941bfbe4410d6865b9b7078e0b49af144d2d',
        '0x4a3411ac2948b33c69666b35cc6d055b27ea84f1',
        -- ETHUSD
        '0xf79d6afbb6da890132f9d7c355e3015f15f3406f',
        '0xb103ede8acd6f0c106b7a5772e9d24e34f5ebc2c',
        '0x00c7a37b03690fb9f41b5c5af8131735c7275446',
        '0xd3fcd40153e56110e6eeae13e12530e26c9cb4fd',
        '0x37bc7498f4ff12c19678ee8fe19d713b87f6a9e6',
        '0xe62b71cf983019bff55bc83b48601ce8419650cc',
        -- LINKUSD
        '0x32dbd3214ac75223e27e575c53944307914f7a90',
        '0xc8b5381a98c7dc8b91f4149303397da56061ebaf',
        '0x8cde021f0bfa5f82610e8ce46493cf66ac04af53',
        '0xbd11bc57fc140614190cabc1b4c316aba220bae4',
        '0xdfd03bfc3465107ce570a0397b247f546a42d0fa',
        '0x20807cf61ad17c31837776fa39847a2fa1839e81',
        '0x96d6e33b411dc1f4e3f1e894a5a5d9ce0f96738d',
        -- USDCUSD
        '0x3b15a92872435c01c27201aae0968839fb45217d',
        '0x789190466e21a8b78b8027866cbbdc151542a26c',
        '0xc9e1a09622afdb659913fefe800feae5dbbfe9d7',
        -- Pool V2 Address
        '0x7d2768de32b0b80b7a3454c06bdac94a69ddc7a9',
        -- Pool V3 Address
        '0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2'
    )
AND 
    topics[SAFE_OFFSET(0)] in (
        -- Aggregator Topic Address
        '0x0559884fd3a460db3073b7fc896cc77986f16e378210ded43186175bf646fc5f',
        -- LiquidationCall event
        '0xe413a321e8681d831f4dbccbca790d2952b56f977908e45be37335533e005286'
    )
ORDER BY block_timestamp DESC
```
