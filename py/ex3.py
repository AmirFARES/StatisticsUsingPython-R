def entry_point(argv):
    S=c(13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73)
    T5=table(cut(S, breaks=c(8,18,28,38,48,58,68,78)))
    T5c=c(T5)
    data.frame(Eff=T5c,EffCum=cumsum(T5c),Freq=T5c/sum(T5c),FreqCum=cumsum(T5c/sum(T5c)))

    hist(S,breaks=c(8,18,28,38,48,58,68,78),xlab="",ylab="",main="",xaxt = "n")
    axis(1, c(8,18,28,38,48,58,68,78))

    y=c(0,0,cumsum(T5c/sum(T5c)),1)
    x=c(0,8,18,28,38,48,58,68,78,88)
    plot(x,y,type="b",xlab="",ylab="",xaxt = "n")
    axis(1, c(8,18,28,38,48,58,68,78))

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