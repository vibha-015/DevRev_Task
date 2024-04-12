## DevRev Snaps TypeScript Template

This repository contains a template for the functions that can be deployed as
part of Snap-Ins.

### Getting started with the template
1. we first C=create a new folder in our device for this template.
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

### Packaging the code
Once we are done with the testing, we run
```
npm install
npm run build
npm run package
```
and ensure it succeeds.

We will see a `build.tar.gz` file is created.
