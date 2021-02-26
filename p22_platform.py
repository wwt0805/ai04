"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2021/2/26 11:36 上午
@Site    :
@File    : p22_platform.py
@Software: PyCharm
"""
import p21_Exp as exp


def solve(exps, lr=0.01, epoches=1000):
    vars = set()  # 变量集合
    derivs = {e: {v: e.deriv(v) for v in e.get_vars()} for e in exps}

    for e in derivs:
        for v in derivs[e]:
            vars.add(v)
    vars = {v: 1.0 for v in vars}

    for _ in range(epoches):
        for e in exps:
            vs = derivs[e]
            ds = {}
            for v in vs:
                deriv = vs[v]
                delta = -lr * deriv.eval(env=vars)
                ds[v] = delta
            for v in vs:
                vars[v] = vars[v] + ds[v]
    return vars


if __name__ == "__main__":
    v = [exp.Variable(chr(ord('a') + i)) for i in range(26)]
    exps = []
    while True:
        s = input('expression = ?')
        if len(s) == 0:
            break
        s = eval(s)
        exps.append(s)
    print(solve(exps))
