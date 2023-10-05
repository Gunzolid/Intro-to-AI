def calculate_cleaning_time(hotel):
    total_cleaning_time = 0

    for floor_number, floor in enumerate(hotel):
        elevator_position = floor.index(-1)  # ตำแหน่งลิฟต์

        # คำนวณเวลาทำความสะอาดสำหรับแต่ละห้องในชั้น
        left_rooms_to_clean = []
        right_rooms_to_clean = []

        # กำหนดด้านที่ใช้เวลาทำความสะอาดน้อยที่สุด
        shortest_path = ""
        if elevator_position != 0 and elevator_position != len(floor) - 1:
            left_time = 0
            right_time = 0

            # คำนวณเวลาทำความสะอาดสำหรับห้องทางด้านซ้ายของลิฟต์
            for room_number, occupants in enumerate(floor[:elevator_position]):
                if room_number != elevator_position and occupants > 0:
                    cleaning_time = 20 + (2 * occupants)
                    left_time += cleaning_time
                    left_rooms_to_clean.append((room_number, cleaning_time))

            # คำนวณเวลาทำความสะอาดสำหรับห้องทางด้านขวาของลิฟต์
            for room_number, occupants in enumerate(floor[elevator_position + 1:]):
                if occupants > 0:
                    cleaning_time = 20 + (2 * occupants)
                    right_time += cleaning_time
                    right_rooms_to_clean.append((room_number + elevator_position + 1, cleaning_time))

            shortest_path = "left" if left_time <= right_time else "right"
            shortest_time = min(left_time, right_time)

            # เรียงลำดับห้องที่ต้องทำความสะอาดในแต่ละด้านตามหมายเลขห้อง
            left_rooms_to_clean.sort(key=lambda x: x[0])
            right_rooms_to_clean.sort(key=lambda x: x[0])

        # คำนวณเวลาทำความสะอาดรวมสำหรับชั้นนี้
        total_floor_cleaning_time = left_time + right_time

        # เพิ่มเวลาทำความสะอาดรวมสำหรับโรงแรมทั้งหมด
        total_cleaning_time += total_floor_cleaning_time

        print(f"\nแผนการทำความสะอาดสำหรับชั้น {floor_number + 1}:")
        if shortest_path == "left":
            print("ลำดับการทำความสะอาดสำหรับด้านซ้าย:")
            for room_number, cleaning_time in left_rooms_to_clean:
                print(f"ห้อง {room_number + 1}: เวลาทำความสะอาด - {cleaning_time} นาที")
            print("ลำดับการทำความสะอาดสำหรับด้านขวา:")
            for room_number, cleaning_time in right_rooms_to_clean:
                print(f"ห้อง {room_number + 1}: เวลาทำความสะอาด - {cleaning_time} นาที")
        else:
            print("ลำดับการทำความสะอาดสำหรับด้านขวา:")
            for room_number, cleaning_time in right_rooms_to_clean:
                print(f"ห้อง {room_number + 1}: เวลาทำความสะอาด - {cleaning_time} นาที")
            print("ลำดับการทำความสะอาดสำหรับด้านซ้าย:")
            for room_number, cleaning_time in left_rooms_to_clean:
                print(f"ห้อง {room_number + 1}: เวลาทำความสะอาด - {cleaning_time} นาที")

        print(f"เส้นทางทำความสะอาดที่สั้นที่สุด: ด้าน {shortest_path}")
        print(f"เวลาการทำงานสำหรับเส้นทางที่สั้นที่สุด: {shortest_time} นาที")
        print(f"เวลาทำความสะอาดรวมสำหรับชั้น: {total_floor_cleaning_time} นาที")

    print(f"\nเวลาทำความสะอาดรวมสำหรับโรงแรมทั้งหมด: {total_cleaning_time} นาที")

# ตัวอย่างโรงแรมที่มี 5 ชั้นและ 5 ห้องในแต่ละชั้น
hotel = [
    [1, 3, -1, 2, 4],
    [2, 5, -1, 4, 1],
    [4, 2, -1, 1, 3],
    [0, 0, -1, 2, 3],
    [1, 4, -1, 0, 1]
]

calculate_cleaning_time(hotel)
