# cronjobs 
Crontab file, depedencies and scripts for miscellaneous jobs running on my home network.

## Usage
Clone the repository with its submodules, and either replace or update `/etc/crontab`.
```
git clone --recursive git@github.com:csabatini/cronjobs.git
cp ./cronjobs/crontab /etc/crontab
```

## Credentials 
Job logs and credentials are stored in the paths `~/.log` and `~/.credentials`.
