def add(*args):
  print(f'type(args)>>> {type(args)}') # <class 'tuple'>
  print(f'args>>> {args}') # args>>> (2, 3, 4, 5, 6, 7)
  print(f'args[3]>>> {args[3]}') # args[3]>>> 5


  for idx in range(len(args)):
    print(f'idx_rng>>> {idx} | rng_args[idx]>>> {args[idx]}')
    # idx_rng>>> 0 | rng_args[idx]>>> 2
    # idx_rng>>> 1 | rng_args[idx]>>> 3
    # idx_rng>>> 2 | rng_args[idx]>>> 4
    # idx_rng>>> 3 | rng_args[idx]>>> 5
    # idx_rng>>> 4 | rng_args[idx]>>> 6
    # idx_rng>>> 5 | rng_args[idx]>>> 7


  idx = 0
  # while idx < len(args):
  #   print(f'idx>>> {idx} | args[idx]>>> {args[idx]}')
    # idx>>> 0 | args[idx]>>> 2
    # idx>>> 1 | args[idx]>>> 3
    # idx>>> 2 | args[idx]>>> 4
    # idx>>> 3 | args[idx]>>> 5
    # idx>>> 4 | args[idx]>>> 6
    # idx>>> 5 | args[idx]>>> 7
    # idx += 1



  sum = 0
  for arg in args:
    sum += arg
    print(f'idx>>> {idx} | args[idx]>>> {args[idx]}')
    # idx>>> 0 | args[idx]>>> 2
    # idx>>> 1 | args[idx]>>> 3
    # idx>>> 2 | args[idx]>>> 4
    # idx>>> 3 | args[idx]>>> 5
    # idx>>> 4 | args[idx]>>> 6
    # idx>>> 5 | args[idx]>>> 7
    idx += 1
    # print(f'arg>>> {arg}')
    # arg>>> 2
    # arg>>> 3
    # arg>>> 4
    # arg>>> 5
    # arg>>> 6
    # arg>>> 7
  print(f'sum>>> {sum}') # sum>>> 27

  for idx, i in enumerate(args):
    print(idx, i)
    for index, item in enumerate(args):
      print(index, item)

  return sum

print(add(2,3,4,5,6,7))