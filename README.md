# cronjobs 
Crontab file and for running various jobs on my home network, with submodules.

## Usage
Clone the repository with its submodules, and either replace or update /etc/crontab
```
git clone --recursive git@github.com:csabatini/cronjobs.git
cp ./cronjobs/crontab /etc/crontab
```

## Credentials 
Any credentials required by the jobs are stored in config files in the `~/.credentials/` directory
