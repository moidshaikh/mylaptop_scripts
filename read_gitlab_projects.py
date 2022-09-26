import gitlab

gl = gitlab.Gitlab(private_token="")
from tqdm import tqdm

# projects = gl.projects.list(get_all=True)


projects = gl.projects.list(iterator=True)



for i, project in tqdm(enumerate(projects)):
    with open(f'project_{i}.json','w') as f:
        print(i, end=' ')
        f.write(str(project))
