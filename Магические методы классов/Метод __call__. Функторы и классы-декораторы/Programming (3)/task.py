class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        if args[0].isdigit():
            return int(args[0])
        elif args[0][0] == '-':
            if args[0][1:].isdigit():
                return int(args[0])


# dg = DigitRetrieve()
#
# st = ["123", "abc", "-56.4", "0", "-5"]
# digits = list(map(dg, st))
# print(digits)