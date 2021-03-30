#!/usr/bin/env python3

from decimal import Decimal, ROUND_HALF_UP

def main():

    # Sample marks in each CA component
    labs = 50
    bucket_list = 100
    labexam_01 = 20
    labexam_02 = 0
    final_ex = 0

    ca = (0.5 * labs) + (1 * bucket_list) + (1.5 * labexam_01) + (2 * labexam_02) + ( 5 * final_ex)
    ca = ca / 10
    

    # Round to nearest integer (with .5 always rounding up)
    ca = int(Decimal(ca).to_integral_value(ROUND_HALF_UP))
    print('Your overall CA mark is: {:d}%'.format(ca))

if __name__ == "__main__":
    main()
