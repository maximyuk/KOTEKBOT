from src.data_base.create_db import BaseDBPart


class UpdateDB(BaseDBPart):
    async def update_student(self, user_id, group_student):
        await self.cur.execute(
            "UPDATE `student` SET `group_student` = ? WHERE user_id = ?",
            (
                group_student,
                user_id,
            ),
        )
        return await self.base.commit()

    async def student_change_news(self, boolean: bool, user_id: int):
        await self.cur.execute(
            "UPDATE `student` SET `send_news` = ? WHERE user_id = ?",
            (
                boolean,
                user_id,
            ),
        )
        return await self.base.commit()

    async def student_change_alert(self, boolean: bool, user_id: int):
        await self.cur.execute(
            "UPDATE `student` SET `send_alert` = ? WHERE user_id = ?",
            (
                boolean,
                user_id,
            ),
        )
        return await self.base.commit()

    async def student_group_photo_update(self, photo, name_group, transl):
        await self.cur.execute(
            "UPDATE `student_group` SET photo = ?, date = ? WHERE name_group = ?",
            (
                photo,
                transl,
                name_group,
            ),
        )
        return await self.base.commit()

    async def update_user(
        self,
        user_id,
        first_name,
        last_name,
        username,
        last_interaction,
        admin,
        student_group,
    ):
        count_interaction = await self.cur.execute(
            "SELECT count_interaction FROM user WHERE user_id = ?", (user_id,)
        )
        count_interaction = await count_interaction.fetchall()
        count_interaction = count_interaction[0][0]
        count_interaction += 1

        await self.cur.execute(
            """UPDATE user 
            SET     
                first_name = ?,    
                last_name = ?,    
                username = ?,    
                count_interaction = ?,  
                last_interaction = ?,  
                admin = ?,   
                student_group = ?
            WHERE user_id = ?
            """,
            (
                first_name,
                last_name,
                username,
                count_interaction,
                last_interaction,
                admin,
                student_group,
                user_id,
            ),
        )
        return await self.base.commit()
