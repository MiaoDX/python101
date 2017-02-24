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