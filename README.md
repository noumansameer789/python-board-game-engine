# Tested Python board-game engine

A compact, deterministic reconstruction of an MSc object-oriented programming
project. The original submission contained 698 lines across seven modules and
25 pytest tests; this portfolio version focuses on the domain boundaries.

`Board`, `Player` and `Game` separate state, movement and turn management.
Seeded randomness, explicit roll injection and defensive validation make the
engine straightforward to test.

```bash
python -m unittest discover -s tests -v
```

This is a clean portfolio reconstruction, not the assessment submission.
