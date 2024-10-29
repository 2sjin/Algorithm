function solution(array) {
    let maximum = Math.max(...array);
    let answer = [maximum, array.indexOf(maximum)];
    return answer;
}