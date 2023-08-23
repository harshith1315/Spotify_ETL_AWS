CREATE EXTERNAL TABLE IF NOT EXISTS `spotifydata`.`spotifydata` (
  `Name` char(50),
  `Artists` char(50),
  `Album` char(50),
  `Release_Date` date
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ('field.delim' = ',')
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.TextInputFormat' OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://spotifybucket7487/data/'
TBLPROPERTIES ('classification' = 'csv');

select * from "spotifydata"."spotifydata"