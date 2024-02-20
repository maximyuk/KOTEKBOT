from src.data_base.create_db import BaseDBPart
from src.data_base.middleprocess import get_number, get_text, get_list


class SelectDB(BaseDBPart):
    async def count_user(self):
        counts = await self.cur.execute("SELECT COUNT(user_id) FROM user")
        return get_number(counts)

    async def count_student(self):
        counts = await self.cur.execute("SELECT COUNT(user_id) FROM student")
        return get_number(counts)

    async def list_id_student_agreed_news(self):
        result = await self.cur.execute("SELECT `user_id` FROM `student` WHERE send_news = ?", (1,))
        return get_list(result)

    async def list_id_student_agreed_alert(self):
        result = await self.cur.execute(
            "SELECT `user_id` FROM `student` WHERE send_alert = ?", (1,)
        )
        return get_list(result)

    async def group_for_student_id(self, user_id):
        name = await self.cur.execute(
            "SELECT `group_student` FROM `student` WHERE `user_id` = ?", (user_id,)
        )
        return get_text(name)

    async def student_group_list(self):
        reslut = await self.cur.execute("SELECT `name_group` FROM `student_group`")
        return sorted(get_list(reslut))

    async def see_rod(self, user_id):
        groups = await self.cur.execute(
            "SELECT `group_student` FROM `student` WHERE `user_id` = ?", (user_id,)
        )
        result = await groups.fetchone()

        photo = await self.cur.execute(
            "SELECT `photo` FROM student_group WHERE name_group = ?", (result[0],)
        )
        rows_photo = await photo.fetchone()
        date = await self.cur.execute(
            "SELECT `date` FROM student_group WHERE name_group = ?", (result[0],)
        )
        rows_date = await date.fetchone()
        try:
            lens = len(rows_photo[0])
        except TypeError:
            lens = 1
        if lens <= 5:
            return False, None, None
        elif lens >= 6:
            reslt = rows_photo[0]
            datka = rows_date[0]
            return True, reslt, datka

    async def see_schedule_student(self, name_group):
        photo = await (
            await self.cur.execute(
                "SELECT `photo` FROM student_group WHERE name_group = ?", (name_group,)
            )
        ).fetchone()
        date = await (
            await self.cur.execute(
                "SELECT `date` FROM student_group WHERE name_group = ?", (name_group,)
            )
        ).fetchone()
        try:
            lens = len(photo[0])
        except:
            lens = 1
        if lens <= 5:
            return False, None, None
        elif lens >= 6:
            reslt = photo[0]
            datka = date[0]
            return True, reslt, datka

    async def see_photo(self, name_photo):
        result = await (
            await self.cur.execute(
                "SELECT id_photo, date_photo FROM photo WHERE name_photo = ?",
                (name_photo,),
            )
        ).fetchone()
        try:
            id_photo = result[0]
            date_photo = result[1]
        except:
            return False, None, None

        return True, id_photo, date_photo

    async def user_show_data(self, user_id):
        result = await self.cur.execute(
            "SELECT * FROM user WHERE user_id = ?",
            (user_id,),
        )
        return await result.fetchall()
