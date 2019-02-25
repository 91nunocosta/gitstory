
GitStory is a simple library to tell git commit histories.

#  Pre-requirements

1. `python3` installed
2. `mongodb` installed and running (see https://docs.mongodb.com/v3.2/administration/install-community/)

# How to run
1. install python requirements, `pip install -r requirements.txt`
2. set environment variables:
    1. ensure that the values in `env.sh` are suitable;
    2. run `source env.sh`
3. run the _gitstory_ script, `python3 gitstory <repo url>`

# How to run tests

1. install pytest, `pip install pytest`
2. run `python3 -m pytest`

Some tests may fail if mongo is not running with the default _host_, `localhost`, and _port_, `27017`.

# TODO

1. Safe parsing of `git log` output. The delimeter char used in the output format can occur in the content. May be overcomed by formatting also with padding. If not, running `git log` to get each column separately would be required.

2. Handling `git log` errors.

3. When getting the commit history using the git CLI, to run `git fetch` if the repository was already cloned. This will ensure that the history is always updated.

4. Follow pagination when using the GitHub API. The current implementation will get only the first page of commits.

5. Encapsulate `GitRepo` factories (`clone`) and the operation of harvesting a remote git repository history using git CLI (`clone`/`fetch` and then `log`), in a `Git` class.
```python
class Git:
    
    def __init__(self, repos_dir):
        ...
       
    def is_cloned(self, repo_url):
        ...
        
    def clone(self, repo_url):
        ...
       
    def fetch(self, repo_url):
        ...
      
    def get_history(self, repo_url):
        if self.is_cloned(repo_url):
            repo = self.fetch(repo_url)
        else
            repo = self.clone(repo_url)
        return repo.log()
```

6. Compose `Github` also with `Git`, in order to make `Github` more extensible.
```python
gitlog_store = MongoGitlogStore(mongo_host, mongo_port, mongo_db)
git_fallback = Git(repos_dir)
Github(gitlog_store, git_fallback)
```
Other fallbacks could be used in the future. Tests will also be a little more clear that way.

7. Configure mongo with environment variables also in the tests. 
