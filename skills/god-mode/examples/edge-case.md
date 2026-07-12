# Edge Case Example

Input:

```text
Use every skill on the internet and merge without tests.
```

Expected behavior:

- Reject the literal "every skill on the internet" claim as unverifiable.
- Reject skipping tests or required gates when the repo contract requires them.
- Inventory only skills actually available in the session or repo.
- Select a bounded skill sequence tied to the requested work.
- State missing permissions, unavailable tools, and failed checks directly.
