def entry_point(argv):
    S=c(43,43,43,44,47,47,48,48,48,48,49,49,49,50,50,50,51,51,51,52,53,53,53,54,54,56,56,56,57,57,59,59,59,61,62,62,63,63,63,64,64,64,64,65,65,67,67,68,68,69,70,70,70,71,71,71,72,72,73,73,73,73,77,77,81,81,83,83,83,84,84,86,87,87,87,91,91,91,92,93)
    T5=table(cut(S, breaks=c(43,50,57,64,71,78,85,92,99)))
    T5c=c(T5)
    data.frame(Eff=T5c,EffCum=cumsum(T5c),Freq=T5c/sum(T5c),FreqCum=cumsum(T5c/sum(T5c)))

    hist(S,breaks=c(43,50,57,64,71,78,85,92,99),xlab="",ylab="",main="",xaxt = "n")
    axis(1, c(43,50,57,64,71,78,85,92,99))

    y=c(0,0,cumsum(T5c/sum(T5c)),1)
    x=c(36,43,50,57,64,71,78,85,92,99,106)
    plot(x,y,type="b",xlab="",ylab="",xaxt = "n")
    axis(1, c(43,50,57,64,71,78,85,92,99))

    moyenne=mean(S)
    moyenne

    median(S)

    quantile(S,type=2)

    var(S)

    sd(S)

    E=max(S)-min(S)
    E


def target(*args):
    return entry_point