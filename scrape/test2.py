import json

test = '{"path": "2019-06-13", "mode": "040000", "type": "tree", "sha": "44c88647005edeef06d4ff0c9e64d48496a41f92", "url": "https://api.github.com/repos/Informatievlaanderen/data.vlaanderen.be-generated/git/trees/44c88647005edeef06d4ff0c9e64d48496a41f92"}, {"path": "2019-10-03", "mode": "040000", "type": "tree", "sha": "fb40468250497625fe9d9106e60be5c7009f6785", "url": "https://api.github.com/repos/Informatievlaanderen/data.vlaanderen.be-generated/git/trees/fb40468250497625fe9d9106e60be5c7009f6785"}, {"path": "2021-12-02", "mode": "040000", "type": "tree", "sha": "a6e0962b8f05fe30709658991416975dafd873dd", "url": "https://api.github.com/repos/Informatievlaanderen/data.vlaanderen.be-generated/git/trees/a6e0962b8f05fe30709658991416975dafd873dd"}, {"path": "2022-04-21", "mode": "040000", "type": "tree", "sha": "acfab7ea358a28b88af3f7682a7b9aff67232e49", "url": "https://api.github.com/repos/Informatievlaanderen/data.vlaanderen.be-generated/git/trees/acfab7ea358a28b88af3f7682a7b9aff67232e49"}'

test = json.loads(str(test))

print(test)