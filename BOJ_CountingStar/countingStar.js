// BOJ 2438번 별찍기-1
function 별찍기1(n){
    for( let i = 1; i < n + 1; i++){
        // i = 1,2,3,4,5
        console.log('*'.repeat(i))
    }
}
별찍기1(5)


// BOJ 2439번 별찍기-2
function 별찍기2(n){
    for( let i = 1; i < n+1; i++){
        //  i = 1,2,3,4,5
        //  n-i = 4,3,2,1,0
        console.log(' '.repeat((n-i)),'*'.repeat(i))
    }
}
별찍기2(5)


// BOJ 2440번 별찍기-3
function 별찍기3(n){
    for( let i = n; i > 0; i--){
        console.log('*'.repeat(i))
    }
}
별찍기3(5)


// BOJ 2441번 별찍기-4
function 별찍기4(n){
    for( let i = n; i > 0; i--){
        // i = 5,4,3,2,1
        // n-i = 0,1,2,3,4
        console.log(' '.repeat((n-i)),'*'.repeat(i))
    }
}
별찍기4(5)


// BOJ 2442번 별찍기-5
function 별찍기5(n){
    for( let i = 0; i < n; i ++){
        // i = 0,1,2,3,4
        // n-1 = 5,4,3,2,1
        console.log(' '.repeat((n-i)-1),'*'.repeat((2*i+1)))
        // (2n+1) 홀수인 점을 이용
    }
}
별찍기5(5)


// BOJ 2443번 별찍기-6
function 별찍기6(n){
    for( let i = n; i > 0; i--){
        // i = 5,4,3,2,1
        // n-i = 0,1,2,3,4
        console.log(' '.repeat((n-i)),'*'.repeat((2*i-1)))
        // i가 n부터 시작하기 때문에 범위를 넘지 않게 (2n-1) 이용
    }
}
별찍기6(5)


// BOJ 2444번 별찍기-7
function 별찍기7(n){
    // 별찍기5번
    for( let i = 0; i < n; i ++){
        console.log(' '.repeat((n-i)-1),'*'.repeat((2*i+1)))
    }
    // 별찍기6번
    for( let i = n-1; i > 0; i--){
        console.log(' '.repeat((n-i)),'*'.repeat((2*i-1)))
    }
}
별찍기7(5)