# Amazon DocumentDB Tools

This repo contains tools to make migrating to Amazon DocumentDB (with MongoDB compatibility) easier.

## Amazon DocumentDB Index Tool 
The Index Tool makes it easier to migrate only indexes (not data) between a source MongoDB deployment and a Amazon DocumentDB cluster. The Index Tool can also help you find potential compatibility issues between your source databases and Amazon DocumentDB. You can use the Index Tool to dump indexes and database metadata, or you can use the tool against an existing dump created with the mongodump tool.

Features:
 - Dump just the indexes from a running mongodb instance/replica set
 - Outputs in the same dump format that mongodump uses
 - Checks indexes, collections, and databases for compatibility with Amazon DocumentDB
 - Checks indexes for unsupported index types
 - Checks collections for unsupported options
 - Restores supported indexes (without data) to Amazon DocumentDB

### Installing
Clone the repository, then run the following command in the repo top-level director:
`pip install -r requirements.txt`

### Using the Index Tool
To dump indexes from a running MongoDB instance or replica set, run the following command:
`python migrationtools/documentdb_index_tool.py --host <host> --port <port> --username <username> --password <password> --auth-db <auth db> --dir <directory to dump metadata to>`

To check for compatibility issues against dumped database metadata, run the following command:
`python migrationtools/documentdb_index_tool.py --show-issues --dir <directory that contains metadata dump>`

To restore only indexes that are compatible with Amazon DocumentDB, run the following command:
`python migrationtools/documentdb_index_tool.py --restore-indexes --dir <directory that contains metadata dump>`

### Command Line Options| 
| Parameter | Type | Description |
|-- |-- |-- |
| `--debug` | flag | _Optional_ output debugging information|
| `--dry-run` | flag | _Optional_ Perform processing, but do not actually restore indexes|
| `--dir` DIR | string | Working directory for intermediate files. During inspection of source cluster, files will be placed in this directory. During restoration, index schema will be read from here.|
| `--show-compatible` | flag | output all compatible indexes (without change)|
| `--show-issues` | flag | Output a detailed structure of compatibility issues|
| `--dump-indexes` | flag | Dump indexes from the specified host/port|
| `--restore-indexes` | flag | Restore indexes found in metadata to the specified host/port|
| `--skip-incompatible` | flag | Skip incompatible indexes while dumping or restoring|
| `--host` HOST | | Connect to host HOST When restoring indexes, this is the target DocumentDB host. Source MongoDB cluster otherwise.(default: localhost)|
| `--port` PORT | | Connect to port PORT When restoring indexes, this is the target DocumentDB host. Source MongoDB cluster otherwise. (default: 27017)|
| `--username` USERNAME | | Authenticate with username USERNAME|
| `--password` PASSEORD | | Authenticate with password PASSWORD|
| `--auth-db` AUTH_DB | string | Authenticate using database AUTH_DB (default: admin)|
| `--tls` | | _Optional_ Connect using TLS|
| `--tls-ca-file` FILE | | Path to CA file used for TLS connection|
| `--tls-client-file` FILE | | Path to client certificate file used for TLS connection. Corresponds to driver's "ssl_certfile"|
| `--tls-pem-passphrase` PASSEORD | | Password to decrypt PEM file if tls-client-file requires a decryption password. Corresponds to driver "ssl_pem_passphrase"|
| `--allow-index-name-shortener` [False] | | _Optional_ Shorten names of indexes that violate index name limits upon `--restore-indexes` (default: True)|

## License

This library is licensed under the Apache 2.0 License. 
