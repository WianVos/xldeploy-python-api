import xldeploy

repo = xldeploy.connect_repository()

print(repo.get_ci_by_name('Infrastructure/test'))