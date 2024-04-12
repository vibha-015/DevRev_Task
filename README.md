## DevRev Snaps TypeScript Template

This repository contains a starter code which was used as a template to build the snap-in. 

### Getting started with the template
1. we first C=create a new folder in our device for this starter code.
2. In the new folder, we can add functions at path `src/functions` where the folder name corresponds to the function name in our manifest file.
3. Each function we add will also need to be mentioned in `src/function-factory.ts` .

### Testing locally
We can test our code by adding test events under `src/fixtures` . We can add keyring values to the event payload to test API calls as well.

Once we have added the event, we can test our code by running:
```
npm install
npm run start:watch -- --functionName=function_1 --fixturePath=function_1_event.json
npm run start:watch -- --functionName=function_2 --fixturePath=function_2_event.json
```

### Adding external dependencies
We can also add dependencies on external packages in package.json under the "dependencies" key. These dependencies will be made available to our function at runtime and testing.

###Authenticate ourselves using the code:
devrev profiles authenticate -o <dev-org-slug> -u <youremail@yourdomain.com>


### Packaging the code
Once we are done with the authenticationg, we run
```
npm install
npm run build
npm run package
```
and ensure it succeeds.

We will see a 'dst' folder and  `build.tar.gz` files are created.

###To create a snap-in package, we run the following command:
devrev snap_in_package create-one --slug my-first-snap-in | jq .

###To create a snap-in version, run the following command:
devrev snap_in_version create-one --path ./devrev-snaps-typescript-template | jq .

###Then we create a snap-in from a snap-in version, run the following command:
devrev snap_in draft

###Deploying the snap-in
We then provide the required configuration for the snap-ins and then click " Deploy snap-in" or "install snap-in" button on the UI. The snap-in should now be active and ready to use.
