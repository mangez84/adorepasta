# Adore Pasta

## Table of Contents

1. [Test](#test)
    - [Validation Services](#validation-services)
        - [W3C Markup Validation Service](#w3c-markup-validation-service)
        - [W3C CSS Validation Service](#w3c-css-validation-service)
        - [JSHint](#jshint)
        - [PEP8 Online](#pep8-online)
    - [Tesing User Stories](#testing-user-stories)
        - [Common Users](#common-users)
        - [Unregistered Users](#unregistered-users)
        - [Registered Users](#registered-users)
        - [Administrator Users](#administrator-users)
    - [Further Testing](#further-testing)
    - [Known Bugs](#known-bugs)
        - [Fixed](#fixed)
        - [Unfixed](#unfixed)

## Test

### Validation Services

#### [W3C Markup Validation Service](https://validator.w3.org/)

- All pages on the website were validated by copying the rendered HTML code from Chrome DevTools and pasting it into the validator.
- The validation tool reported no errors or warnings. 

#### [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

- The CSS code was validated using direct input mode.
- The validation tool reported no errors after checking the CSS code.
- A warning is displayed stating that imported stylesheets are not validated in direct input mode.

#### [JSHint](https://jshint.com/)

- JSHint did not report any errors or warnings when validating the JavaScript code.
- JSHint was configured with the following settings during validation.

    ```
    /* jshint esversion: 8 */ 
    /* globals $:false */
    ```

#### [PEP8 Online](http://pep8online.com/)

- The tool did not report any warnings or errors after validating the Python code for PEP8 compliance.

### Testing User Stories

#### Common Users

#### Unregistered Users

#### Registered Users

#### Administrator Users

### Further Testing

### Known Bugs

#### Fixed

#### Unfixed

Back to main [README](README.md) file.