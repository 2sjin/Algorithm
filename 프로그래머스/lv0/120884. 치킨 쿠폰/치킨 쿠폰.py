def solution(chicken):
    # 처음 시킨 시킨
    total_service = 0
    coupon = chicken
    
    # 서비스로 시킨 치킨(쿠폰이 10개 미만일 때 까지)
    while coupon >= 10:
        current_service = coupon // 10      # 지금 서비스로 치킨 시킨 수
        total_service += current_service    # 총 서비스 치킨 수
        coupon -= current_service * 9       # 쿠폰 9개 감소(10개 주고 1개 받으므로)
    
    return total_service