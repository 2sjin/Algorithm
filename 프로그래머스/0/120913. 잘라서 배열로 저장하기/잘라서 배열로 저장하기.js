function solution(my_str, n) {
    let push_str;
    var answer = [];
    
    for (let i=0; i<my_str.length; i+=n) {
        push_str = my_str.slice(i, i+n)
        answer.push(push_str);
    }

    return answer;
}