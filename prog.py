
import argparse as arg

from typing import Optional

from fastapi import FastAPI

#import uvicorn

app = FastAPI()

#print(arg.__doc__)
@app.get("/")
def read_root():
    parser=arg.ArgumentParser()
    parser.add_argument("-v", "--verbose",help ="verbosity state", action="store_true")
    parser.add_argument("-q", "--quiet", help="quiet state",action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args=parser.parse_args()
    answer=args.x**args.y
    if args.verbose:
        return{f"{args.x} power to {args.y} equals {answer}"}
    elif args.quiet:
        return{f"{args.x}^{args.y}={answer}"}
    else:
        return {"{} is the result of {} power to {}" .format(answer, args.x, args.y)}

#if __name__=="__main__":
#    uvicorn.run(app, port=80, host="0.0.0.0")



#parser.add_argument("square", type=int, help="display a square of a given number")
#parser.add_argument("echo", help="echo the string you use here")
#args =parser.parse_args()
#answer=args.square**2
#echostring=args.echo
#if args.verbose >= 2:
#    print(f"the square of {args.square} equals {answer}")
#elif args.verbose >= 1:
#    print(answer)
#    print(f"{args.square}^2 == {answer}")
#else: 
#    print(echostring)
#    print(answer)



#parser =arg.ArgumentParser()
#parser.add_argument("-v", "--verbose", help ="increase output verbosity", action="count", default =0)
#parser.add_argument("x", type=int, help="the base")
#parser.add_argument("y", type=int, help="the exponent")
#args=parser.parse_args()
#answer=args.x**args.y
#if args.verbose >=2:
#    print(f"{args.x} power to {args.y} equals {answer}")
#elif args.verbose >=1:
#    print(f"{args.x}^{args.y} = {answer}")
#else:
#    print(answer)

