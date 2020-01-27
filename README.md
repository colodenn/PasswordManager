# PasswordManager

  

## Git Strategy

  

The repository origin consists of the permanent main branches:

- master (protected)

- develop

The content of the master branch always represents the lastly released source code. In develop you

will always find the latest changes that are planned for the release. As the changes are released off of

develop, they are also merged with master and provided with a release tag at the same time.

  

### Feature branches

  

The project is then worked on via a number of feature branches with limited lifetimes. A seperate

branch can be opened for each feature, allowing multiple developers to work simultaneously on different aspects of the project. The feature branches are always branched off from develop and are

also merged back to develop when the feature is completed. The feature branches are usually not

maintained in origin, but are created and managed exclusively in the local repo of the developer. This

can be achieved with the following command:

```bash
$ git checkout -b feature_XXXX develop 
```

_The naming convention for feature branches is feature_XXXX_, whereby the part after the underscore

should represent a short but appropriate name for the respective feature. Once the feature is developed, it must be merged back to develop and can then be pushed to origin/develop:
```bash
$ git checkout develop
```
_Switched to branch 'develop'_
```bash
$ git merge --no-ff feature_XXXX
```
_Updating ea1b82a..05e9557_

_(Summary of changes)_
```bash
$ git branch -d myfeature
```
_Deleted branch myfeature (was 05e9557)._
```bash
$ git push origin develop
```
### Release branches

The release is handled via separate branches, which are used to make last-minute changes and update the version number. Like the feature branches, release branches are branched off from develop

exactly at the point in time at which the release-ready state is in develop. The following command

can be used analogous to the features:
```bash
$ git checkout -b release_X.X develop
```
The naming convention stipulates that the underscore is followed by the version number. When

completely new features are released, the number before the dot is incremented, when features are

added that extend or improve other existing features, the number after the dot is incremented. The

commit is always characterized by the following commit message:
```bash
$ git commit -a -m "Bumped version number to X.X"
```
At the end of the release, the branch is merged back to develop and the tag is created:
```bash
$ git checkout develop
```
Switched to branch 'develop'
```bash
$ git merge --no-ff release_X.X
```
Merge made by recursive.

(Summary of changes)
```bash
$ git tag X.X
```
```bash
$ git push origin develop
```
Lastly, the local release branch can be deleted again:
```bash
$ git branch -d release_X.X
```
Now a corresponding merge-request should be sent to the repo owner of origin to merge this state

of develop with master
```