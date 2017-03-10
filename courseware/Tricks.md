## Notes and takeaways & Convention(惯例) <-> pythonic

* In text editor, make `tab` as `blank`
* In stead of `lowerCaseLikeACamel`, use `lower_case_with_underscores`
* Index starts from `0`
* Tuples are like lists but are immutable.
``` python
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError
```
* main function

``` python
if __name__ == '__main__':
    main()
```

Useful when using `import`

* pip freeze or list to find out installed libs
* `li[1:-1:2]`
    
    use `-1` to avoid calc the length of list.

* usage of `_`:

[what-is-the-purpose-of-the-single-underscore-variable-in-python](http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python):


>
_ has 3 main conventional uses in Python:
>>
    To hold the result of the last executed statement in an interactive interpreter session. This precedent was set by the standard CPython interpreter, and other interpreters have followed suit
    For translation lookup in i18n (see the gettext documentation for example), as in code like: raise forms.ValidationError(_("Please enter a correct username"))
    As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored, as in code like: label, has_label, _ = text.partition(':')
>
The latter two purposes can conflict, so it is necessary to avoid using _ as a throwaway variable in any code block that also uses it for i18n translation (many folks prefer a double-underscore, __, as their throwaway variable for exactly this reason).
