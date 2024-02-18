from pydriller import Repository





def init()->dict:
    repository_init = {"path_to_repo":"C://SourceCode//test//self","from_commit":"860a37ba0d689ffa7343ad2025fabe793149261f","include_remotes":True,"include_refs":True}
    return repository_init

def fetch_add_commits():
    pass


def main():
    repo_dict = init()
    repo = Repository(**repo_dict)
    commit_hash = []
    for commit in repo.traverse_commits():
        commit_hash.append(commit.hash)

    
    for commit in commit_hash:
        print(commit)
    print(len(commit_hash))
    if "f0a0ab3c08ab204ebe628e29939417f4b79b377b" in commit_hash:
        print("yes")

if __name__=="__main__":
    main()
