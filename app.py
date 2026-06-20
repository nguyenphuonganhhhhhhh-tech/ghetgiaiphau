import streamlit as st
from pathlib import Path
from PIL import Image

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Ghét Giải Phẫu",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Ghét Giải phẫu")
st.caption("Sinh viên nhập đáp án theo từng số. Sau khi nhấn Enter, đáp án đúng sẽ hiện ngay bên dưới.")

# =========================
# DỮ LIỆU TRẠM
# Bạn chỉ cần sửa phần này:
# - image: tên file ảnh trong thư mục images
# - answers: số thứ tự và đáp án đúng
# =========================
STATIONS = [
    {
        "name": "Trạm 1",
        "image": "1.png",
        "answers": {
                "1": "lỗ tịt",
   		"2": "lỗ sàng",
    		"3": "lỗ ống tk thị giác",
    		"4": "lỗ tròn",
    		"5": "lỗ bầu dục",
    		"6": "lỗ rách",
    		"7": "lỗ ống tai trong",
    		"8": "lỗ tm cảnh trong",
   		"9": "lỗ ống tk hạ thiệt",
    		"10": "mỏm yên trước",
    		"11": "lưng yên",
    		"12": "ụ chẩm trong",
    		"13": "rãnh xoang ngang",
    		"14": "rãnh xoang sigma",
    		"15": "mào gà",
    		"16": "mào chẩm trong",
    		"17": "rãnh xoang đá trên",
    		"18": "trần ổ mắt",
		"19": "ách bướm",
		"20": "cánh nhỏ xương bướm"
        }
    },
    {
        "name": "Trạm 2",
        "image": "2.png",
        "answers": {
            "1.1": "hành khứu",
            "1.2": "dải khứu",
            "2": "rãnh td chẩm ",
            "3": "rãnh bên phụ",
	    "4": "hồi cạnh hải mã",
	   "5": "hồi thẳng"
        }
    },
    {
        "name": "Trạm 3",
        "image": "3.png",
        "answers": {
                "1.1": "rãnh đai",
   		"1.2": "rãnh dưới đỉnh",
    		"2": "rãnh thể chai",
    		"3.1": "mỏ thể chai",
    		"3.2": "gối thể chai",
		"3.3": "thân thể chai",
		"3.4": "lồi thể chai",
		"4": "rãnh đỉnh chẩm",
		"5": "rãnh cựa",
    		"6.1": "hồi đai",
		"6.2": "hồi chêm",
		"6.3": "hồi lưỡi",
		"6.4": "tiểu thuỳ trung tâm",
    		"7.1": "đồi thị",
		"7.2": "mép dính gian đồi thị",
    		"8": "vòm não",
   		"9": "vách trong suốt",
    		"10": "vùng hạ đồi",
    		"11": "lỗ gian não thất",
		"12": "mép trước"
        }
    },
    {
        "name": "Trạm 4",
        "image": "4.jpg",
        "answers": {
                "1": "rãnh trung tâm",
    		"2": "rãnh bên",
    		"3.1": "rãnh trước trung tâm",
    		"3.2": "rãnh sau trung tâm",
		"4.1": "rãnh trán trên",
		"4.2": "rãnh trán dưới",
		"5.1": "rãnh thái dương trên",
		"5.2": "rãnh thái dương dưới",
    		"6": "rãnh nội đỉnh",
    		"7": "rãnh đỉnh chẩm"
		
        }
    },
    {
        "name": "Trạm 5",
        "image": "5.jpg",
        "answers": {
                "1": "cơ chẩm trán",
    		"2": "cơ mảnh khảnh",
    		"3": "cơ vòng mắt",
    		"3.1": "phần mí",
		"3.2": "phần mắt",
		"4": "cơ mũi",
		"5": "cơ nâng môi trên",
    		"6": "cơ gò má bé",
		"7": "cơ gò má lớn",
		"8": "cơ vòng miệng",
		"9": "cơ mút",
    		"10": "cơ cười",
		"11": "cơ hạ môi dưới",
		"12": "cơ hạ góc miệng",
		"13": "cơ cằm",
    		"14": "cơ ức đòn chũm",
		"14.1": "phần ức",
    		"14.2": "phần đòn"	
        }
    },
    {
        "name": "Trạm 6",
        "image": "6.jpg",
        "answers": {
		"1": "cơ thái dương",
    		"2": "đm thái dương nông",
    		"3": "đm ngang mặt",
		"4": "đm góc",
		"5": "đm môi trên",
    		"6": "đm môi dưới",
		"7": "cơ mút",
		"8": "đm chẩm",
		"9": "đm cảnh trong",
    		"10": "đm cảnh ngoài",
		"11": "đm cảnh chung",
		"12": "tk mặt",
		"13": "đm mặt",
    		"14": "đm lưỡi",
		"15": "đm thanh quản",
		"16": "cơ giáp móng",
    		"17": "đm giáp trên",
    		"18": "cơ bậc thang",
		"18.1": "cơ bậc thang trước",
		"18.2": "cơ bậc thang giữa",
		"18.3": "cơ bậc thang sau",
		"19": "cơ nâng vai",
		"20": "tm cảnh trong",
    		"21": "tm dưới đòn",
		"22": "tm cảnh ngoài",
    		"23": "đm dưới đòn",
    		"24": "đám rối tk cánh tay",
		"25": "cơ bán gai đầu"	
        }
    },
    {
        "name": "Trạm 7",
        "image": "7.jpg",
        "answers": {
		"1": "nhánh thái dương nông đm cảnh ngoài",
    		"2": "cơ tai trên",
    		"3": "cơ tai trước",
		"4": "tuyến nước bọt mang tai",
		"5": "ống tuyến mang tai",
    		"6": "cơ cắn",
		"7": "nhánh mặt đm cảnh ngoài",
		"8": "cơ gối đầu",
		"9": "cơ ức đòn chũm",
    		"10": "cơ nâng vai",
		"11": "cơ thang",
		"12": "cơ vai móng",
		"13.1": "cơ bậc thang giữa",
		"13.2": "cơ bậc thang sau",
		"13.3": "cơ bậc thang trước",
    		"14": "tm cảnh ngoài",
		"15": "đm dưới đòn"
		}
    },

    {
        "name": "Trạm 9",
        "image": "9.jpg",
        "answers": {
                "1": "liềm đại não",
    		"2.1": "thể chai",
    		"2.2": "vòm não",
		"2.3": "vách trong suốt"
		
        }
    },
    {
        "name": "Trạm 10",
        "image": "10.jpg",
        "answers": {
                "1.1": "cơ hàm móng",
    		"1.2": "cơ cằm móng",
    		"2.1": "cơ trâm móng",
		"2.2": "cơ trâm lưỡi",
		"3": "tiền đình miệng",
		"4.1": "tuyến nước bọt dưới hàm",
		"4.2": "tuyến nước bọt dưới lưỡi",
		"5.1": "thềm mũi",
		"5.2": "ngách mũi",
		"5.3": "xoăn mũi"
		
        }
    },
    {
        "name": "Trạm 11",
        "image": "11.jpg",
        "answers": {
               	"1": "rãnh đai",
    		"2": "rãnh dưới đỉnh",
    		"3": "rãnh thể chai",
		"4": "rãnh đỉnh chẩm",
		"5": "rãnh cựa",
    		"6": "tiểu thuỳ cạnh trung tâm",
		"7": "hồi đai",
		"8": "hồi chêm",
		"9": "hồi lưỡi",
    		"10.1": "mỏ thể chai",
		"10.2": "gối thể chai",
		"10.3": "thân thể chai",
		"10.4": "lồi thể chai",
		"11": "vách trong suốt",
		"12": "vòm não",
		"13": "đồi thị",
		"13.1": "mép dính gian đồi thị",
    		"14": "vùng hạ đồi",
		"15": "lỗ gian não thất",
		"16": "mép trước",
    		"17": "thể tùng",
    		"18": "mép sau",
		"19": "não thất IV",
		"20": "tiễu não"
		
        }
    },
    {
        "name": "Trạm 14",
        "image": "14.jpg",
        "answers": {
                "1": "củ não sinh tư",
    		"2": "tuyến tùng",
    		"3": "dây tk ròng rọc",
		"4": "tam giác lang thang",
		"5": "tam giác hạ thiệt",
		"6": "gò tk mặt",
		"7": "diện tiền đình",
		"8": "vân tuỷ não thất IV",
		"9": "màn tuỷ trên"
		
        }
    },
    {
        "name": "Trạm 17",
        "image": "17.jpg",
        "answers": {
                "1.1": "thân xg móng",
    		"1.2": "sừng bé xg móng",
		"1.3": "sừng lớn xg móng",
    		"2.1": "mảnh sụn giáp",
		"2.2": "lồi thanh quản",
		"2.3": "khuyết giáp trên",
		"3": "sụn nhẫn",
		"4": "sụn khí quản",
		"5.1": "tuyến giáp",
		"5.2": "eo tuyến giáp",
		"5.3": "thuỳ tuyến giáp",
		"6": "màng giáp móng",
		"8": "đm giáp trên",
		"9": "tm giáp dưới"
        }
    },
    {
        "name": "Trạm 18",
        "image": "18.jpg",
        "answers": {
                "1.1": "cơ phễu ngang",
    		"1.2": "cơ phễu chéo",
    		"1.3": "cơ nhẫn phễu sau",
		"2": "mảnh sụn nhẫn",
		"3": "sụn thượng thiệt",
		"4": "ngách hình lê"	
        }
    },
    {
        "name": "Trạm 19",
        "image": "19.jpg",
        "answers": {
                "1": "đường hàm móng",
    		
    		"2": "lỗ hàm dưới",
		"3": "gai cằm"
        }
    },
    {
        "name": "Trạm 20",
        "image": "20.jpg",
        "answers": {
                "1.1": "mỏm lồi cầu",
    		"1.2": "chỏm lồi cầu",
    		"1.3": "hố chân bướm",
		"2": "mỏm vẹt",
		"3": "khuyết hàm dưới",
		"4.1": "góc hàm dưới",
		"4.2": "ngành hàm dưới",
		"5": "đường chếch",
		"6": "lỗ cằm",
		"7.1": "ụ cằm",
		"7.2": "củ cằm"
		
        }
    },
    {
        "name": "Trạm 22",
        "image": "22.jpg",
        "answers": {
                "1.1": "thân đm phổi",
    		"1.2": "cung đm chủ",
    		"1.3": "tm chủ trên",
		"2.1": "rãnh vành",
		"2.2": "đm vành phải",
		"3": "đm gian thất trước",
		"4": "nón đm",
		"5.1": "tiểu nhĩ phải",
		"5.2": "tiểu nhĩ trái",
		"6": "đỉnh tim",
		"7": "rãnh gian thất trước"
		
        }
    },
    {
        "name": "Trạm 23",
        "image": "23.jpg",
        "answers": {
                "1.1": "tâm nhĩ phải",
    		"1.2": "tâm nhĩ trái",
    		"2.1": "đm phổi",
		"2.2": "tm phổi P",
		"3.1": "tm chủ trên",
		"3.2": "tm chủ dưới",
		"4": "xoang vành",
		"5.1": "tm bờ trái",
		"5.2": "tm tim giữa",
		"5.3": "tm tim lớn",
		"6": "đm gian thất sau"
		
        }
    },
    {
        "name": "Trạm 24",
        "image": "24.jpg",
        "answers": {
                "1.1": "đm phổi",
    		"1.2": "đm chủ",
    		"2.1": "tm chủ trên",
		"2.2": "tm chủ dưới",
		"3.1": "rãnh vành",
		"3.2": "đm vành phải",
		"4.1": "tiểu nhĩ phải",
		"4.2": "tâm nhĩ phải"
        }
    },
    {
        "name": "Trạm 25",
        "image": "25.jpg",
        "answers": {
                "1.1": "van đm phổi",
    		"1.2": "van đm chủ",
    		"2": "vách gian thất",
		"2.2": "cơ trâm lưỡi",
		"3.2": "cầu cơ",
		"3.3": "cơ nhú",
		"4": "tâm nhĩ phải",
		"5.1": "tâm thất phải",
		"5.2": "tâm thất trái"
        }
    },
    {
        "name": "Trạm 27",
        "image": "27.jpg",
        "answers": {
                "1": "tm đơn",
    		"2.1": "tm cánh tay đầu trái",
		"2.2": "tm cánh tay đầu phải",
		"3": "thân đm cánh tay đầu",
		"4": "đm cảnh chung trái",
		"5.1": "đm phổi phải",
		"5.2": "đm phổi trái",
		"6.1": "tm chủ trên",
		"6.2": "tm chủ dưới",
		"7": "xoang đm vành",
		"8.1": "tm bờ trái",
		"8.2": "tm tim giữa",
		"9": "đm gian thất sau"	
        }
    },
    {
        "name": "Trạm 28",
        "image": "28.jpg",
        "answers": {
                "1.1": "sụn giáp",
    		"1.2": "màng giáp móng",
		"1.3": "màng nhẫn giáp",
    		"2.1": "đm cảnh chung phải",
		"2.2": "đm cảnh chung trái",
		"3.1": "tm cảnh trong phải",
		"3.2": "tm cảnh trong trái",
		"4.1": "tm cánh tay đầu phải",
		"4.2": "tm cánh tay đầu trái",
		"5": "cung đm chủ",
		"6": "thân đm phổi",
		"7.1": "khe ngang",
		"7.2": "khe chếch"
        }
    },
    {
        "name": "Trạm 29",
        "image": "29.jpg",
        "answers": {
                "1": "khí quản",
    		"2.1": "phế quản chính phải",
		"2.2": "phế quản chính trái",
		"4": "tm đơn",
		"5.1": "đm phổi",
		"5.2": "tm phổi",
		"6": "tm chủ trên",
		"7": "thực quản",
		"8": "đm chủ ngực"
		
        }
    },
    {
        "name": "Trạm 30",
        "image": "30.jpg",
        "answers": {
                "1": "tháp thận",
    		"2": "nhú thận",
		"3": "tiểu thùy vỏ",
		"4": "diện sàng",
		"5": "xoang thận",
		"5.1": "đài lớn",
		"5.2": "đài bé",
		"5.3": "bể thận",
		"6.1": "đm thận",
		"6.2": "tm thận",
		"7": "đm gian thuỳ",
		"8": "đm gian tiểu thuỳ",
		"9": "đm cung",
		"10": "niệu quản"
		
        }
    },
    {
        "name": "Trạm 31",
        "image": "31.jpg",
        "answers": {
                "1": "niệu quản",
    		"2": "tuyến thượng thận",
		"3": "cơ vuông thắt lưng",
		"4": "cơ thắt lưng lớn",
		"5": "cơ chậu",
		"6": "cơ ngang bụng",
		"7": "đm chủ bụng",
		"8": "tm chủ dưới"	
        }
    },
    {
        "name": "Trạm 32",
        "image": "32.jpg",
        "answers": {
                "1": "dc tròn",
    		"2": "dc rộng",
		"3": "vòi tử cung",
		"3.1": "bóng tử cung",
		"3.2": "phễu tử cung",
		"3.3": "eo vòi tử cung",
		"4": "nếp rốn trong",
		"5": "dc riêng buồng trứng",
		"6": "cơ thẳng bụng"	
        }
    },
    {
        "name": "Trạm 33",
        "image": "33.jpg",
        "answers": {
                "1": "đỉnh bàng quang",
    		"2": "đáy bàng quang",
		"3": "mặt trên bàng quang",
		"4": "niệu quản",
		"5": "ống dẫn tinh"
		
        }
    },
    {
        "name": "Trạm 34",
        "image": "34.jpg",
        "answers": {
                "1": "tuyến tinh",
    		"2": "bóng ống dẫn tinh",
		"3": "tuyến tiền liệt",
		"4.1": "mặt dưới bên bàng quang"
        }
    },
    {
        "name": "Trạm 35",
        "image": "35.jpg",
        "answers": {
                "1.1": "đáy tử cung",
    		"1.2": "mặt trên tử cung",
		"1.3": "mặt dưới tử cung",
		"1.4": "buồng tử cung",
		"1.5": "cổ tử cung",
		"1.6": "ống cổ tử cung",
    		"2.1": "túi cùng Douglas",
		"2.2": "túi cùng bàng quang",
		"3.1": "âm đạo",
		"3.2": "lỗ âm đạo",
		"3.3": "vòm âm đạo",
		"4": "đỉnh bàng quang",
		"5.1": "đáy bàng quang",
		"5.2": "dc rốn giữa",
		"6.1": "mặt trên bàng quang",
		"6.2": "mặt dưới bên bàng quang",
		"7.1": "lỗ niệu đạo trong",
		"7.1": "lỗ niệu đạo ngoài",
		"8.1": "âm vật",
		"8.2": "môi bé",
		"9.1": "trực tràng",
		"9.2": "ống hậu môn",
		"10.1": "cơ thắt hậu môn trong",
		"10.2": "cơ thắt hậu môn ngoài"
		
        }
    },
    {
        "name": "Trạm 43",
        "image": "43.jpg",
        "answers": {
                "1.1": "quy đầu",
    		"1.2": "thân dương vật",
    		"1.3": "rễ dương vật",
		"2.1": "tinh hoàn",
		"2.2": "đm tinh hoàn",
		"2.3": "tm tinh hoàn",
		"3.1": "mào tinh",
		"3.2": "ống dẫn tinh",
		"4": "mặt dưới bên bàng quang",
		"5": "tuyến tiền liệt",
		"6": "niệu quản đoạn bụng"
		
        }
    },
    {
        "name": "Trạm 44",
        "image": "44.jpg",
        "answers": {
                "1": "đỉnh bàng quang",
    		"2.1": "đáy bàng quang",
    		"2.2": "dc rốn giữa",
		"4.1": "lỗ niệu đạo trong",
		"4.2": "lỗ niệu đạo ngoài",
		"5.1": "vật hang",
		"5.2": "vật xốp",
		"5.3": "quy đầu",
		"6.1": "cơ thắt hậu môn trong",
		"6.2": "cơ thắt hậu môn ngoài",
		"7.1": "tuyến tiền liệt",
		"7.2": "túi bầu dục",
		"8": "tuyến hành niệu đạo"
		
        }
    },
    {
        "name": "Trạm 36",
        "image": "36.jpg",
        "answers": {
                "1.1": "lá phải của dc liềm",
    		"1.2": "lá trái của dc liềm",
    		"2.1": "thuỳ phải",
		"2.2": "thuỳ trái",
		"3": "khuyết dc tròn",
		"4": "đáy túi mật"
        }
    },
    {
        "name": "Trạm 37",
        "image": "37.png",
        "answers": {
                "1": "vùng trần",
    		
    		"2.1": "dc vành",
		
		"3": "tm chủ dưới",
		"4": "tm gan trái"
		
		
        }
    },
    {
        "name": "Trạm 38",
        "image": "38.png",
        "answers": {
                "1": "thuỳ vuông",
    		"2": "thuỳ đuôi",
    		"3.1": "ấn dạ dày",
		"3.2": "ấn đại tràng",
		"3.3": "ấn thận",
		"3.4": "ấn tá tràng",
		"3.5": "ấn thực quản",
		"3.6": "ấn thượng thận",
		"4": "dc tròn",
		"5": "khe dc tm",
		"6.1": "đáy túi mật",
		"6.2": "thân túi mật",
		"6.3": "cổ túi mật",
		"6.4": "ống túi mật",
		"7": "tm cửa",
		"8": "đm gan riêng"
		
        }
    },
    {
        "name": "Trạm 39",
        "image": "39.png",
        "answers": {
                "1.1": "bướu đại tràng",
    		"1.2": "dải mạc nối",
    		"1.3": "dải tự do",
		"2.1": "đm mạc treo tràng trên",
		"2.2": "tm mạc treo tràng trên",
		"3.1": "hồi tràng",
		"3.2": "góc hồi manh tràng",
		"4": "đm sigma",
		"4.1": "kết tràng sigma",
		"4.2": "đm trực tràng trên",
		"5": "đm đại tràng phải",
		"6": "đm lách",
		"7": "đm mạc treo tràng dưới"	
        }
    },
    {
        "name": "Trạm 40",
        "image": "40.png",
        "answers": {
                "1": "tm lách",
    		"2": "tm cửa",
    		"1.3": "dải tự do",
		"3": "ống mật chủ",
		"4": "tm mạc treo tràng trên",
		
		"5": "đm mạc treo tràng trên",
		"6": "tm mạc treo tràng dưới"
		
        }
    },
    {
        "name": "Trạm 41",
        "image": "41.png",
        "answers": {
                "1.1": "tm lách",
    		"1.2": "tm mạc treo tràng dưới",
    		"1.3": "tm mạc treo tràng trên",
		"2.1": "đm mạc treo tràng trên",
		
		"3.1": "phần trên tá tràng",
		"3.2": "phần xuống tá tràng",
		"3.3": "phần nặng tá tràng",
		"3.4": "phần lên tá tràng",
		
		"4.1": "đm tá tuỵ trên sau",
		"4.2": "đm tá tuỵ dưới sau",
		"5": "ống mật chủ",
		"6": "lách",
		"7.1": "đầu tuỵ"	,
		"7.2": "đuôi tuỵ",
		"8": "túi mật"
        }
    },
    {
        "name": "Trạm 42",
        "image": "42.png",
        "answers": {
                "1.1": "đm thân tạng",
    		"1.2": "đm lách",
    		"1.3": "đm gan chung",
		"1.4": "đm gan riêng",
		"2": "đm tá tuỵ trên trước",
		"3": "đm tá tuỵ dưới trước",
		
		
		"4.1": "đm mạc treo tràng trên",
		"4.2": "tm mạc treo tràng trên",
		"5.1": "ống gan phải",
		"5.2": "ống gan trái",
		"5.3": "ống gan chung",
		"5.4": "ống mật chủ",
		"5.5": "ống túi mật",
		"7": "ống tuỵ chính",
		"7.2": "ống tuỵ phụ",
		"7.3": "bóng gan tuỵ",
		"8.1": "nhú tá lớn",
		"8.2": "nhú tá bé",
		"9": "mỏm móc",
		"10.1": "bờ răng cưa của lách",
		"10.2": "ấn dạ dày",
		"11": "hỗng tràng",
		"12": "tm cửa"
			
        }
    },
    {
        "name": "Trạm 45",
        "image": "45.jpg",
        "answers": {
                "1": "bờ cong bé",
    		"2": "bờ cong lớn",
    		"3": "tâm vị",
		"4": "lỗ tâm vị",
		"5": "khuyết góc",
		"6.1": "vòng mạch bờ cong lớn",
		"6.2": "vòng mạch bờ cong bé"
        }
    },
    {
        "name": "Trạm 46",
        "image": "46.png",
        "answers": {
                "1": "cơ dọc",
    		"2": "cơ vòng",
    		"3": "khuyết góc",
		"4": "khuyết tâm vị",
		"5": "tk lang thang",
		"6": "tâm vị",
		"7": "đáy vị",
		"8": "môn vị"
        }
    },
    {
        "name": "Trạm 47",
        "image": "47.jpg",
        "answers": {
                "1": "nếp vị",
    		"2": "lỗ tâm vị",
    		"3": "cơ thắt môn vị",
		"4": "lớp thanh mạc"
		
        }
    },
]

IMAGE_DIR = Path(".")

# =========================
# HÀM TIỆN ÍCH
# =========================

def normalize_answer(text: str) -> str:
    return text.strip().lower()

if "station_index" not in st.session_state:
    st.session_state.station_index = 0

station_index = st.session_state.station_index
station = STATIONS[station_index]

st.sidebar.header("⚙️ Cài đặt")
st.sidebar.write(f"Đang ở: **{station['name']}**")

show_all_answers = st.sidebar.checkbox("Hiện toàn bộ đáp án cho giảng viên", value=False)

if st.sidebar.button("🔄 Làm lại trạm này"):
    for key in list(st.session_state.keys()):
        if key.startswith(f"answer_{station_index}_"):
            del st.session_state[key]
    st.rerun()

st.subheader(station["name"])

col1, col2 = st.columns([1.2, 1])

with col1:
    image_path = IMAGE_DIR / station["image"]

    if image_path.exists():
        img = Image.open(image_path)
        st.image(img, use_container_width=True)
    else:
        st.warning(f"Chưa có ảnh: {image_path}")

with col2:
    st.markdown("### ✍️ Nhập đáp án")

    for number, correct_answer in station["answers"].items():
        st.markdown(f"**Số {number}:**")

        user_answer = st.text_input(
            "Nhập đáp án",
            key=f"answer_{station_index}_{number}",
            placeholder="Nhập đáp án rồi nhấn Enter...",
            label_visibility="collapsed"
        )

        if user_answer.strip():
            if normalize_answer(user_answer) == normalize_answer(correct_answer):
                st.success(f"✅ Đúng. Đáp án: {correct_answer}")
            else:
                st.error(f"❌ Đáp án đúng: {correct_answer}")

        st.markdown("---")

    if st.button("➡️ Chuyển sang trạm tiếp theo"):
        if st.session_state.station_index < len(STATIONS) - 1:
            st.session_state.station_index += 1
            st.rerun()
        else:
            st.success("🎉 Đã hoàn thành tất cả các trạm!")

    if st.button("⬅️ Quay lại trạm trước"):
        if st.session_state.station_index > 0:
            st.session_state.station_index -= 1
            st.rerun()

if show_all_answers:
    st.markdown("## 🔐 Đáp án toàn bộ trạm")
    for number, correct_answer in station["answers"].items():
        st.write(f"**{number}.** {correct_answer}")
