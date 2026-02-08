from dataclasses import dataclass

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

p = ImmutablePoint(10, 20)
print(p)

# Любая попытка изменить атрибут вызовет ошибку!
try:
    p.x = 30
except Exception as e:
    print(f"\nОшибка при попытке изменить p.x: {e}")