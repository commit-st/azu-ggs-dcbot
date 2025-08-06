 # cogs/announce.py

-    async def announce(
-        self,
-        interaction: discord.Interaction,
-        color: str,
-        title: str,
-        content: str
-    ):
+    async def announce(
+        self,
+        interaction: discord.Interaction,
+        color: str,
+        title: str,
+        content: str
+    ):
+        # 색상 파싱
+        try:
+            c = int(color.lstrip("#"), 16)
+        except ValueError:
+            return await interaction.response.send_message(
+                "❌ 유효한 색상 코드를 입력하세요. ex) #FF69B4",
+                ephemeral=True
+            )
+        # 구분선 생성
+        separator = "─" * 30
+        # Embed 생성
+        embed = discord.Embed(
+            title=title,
+            description=f"{separator}\n{content}",
+            color=discord.Color(c)
+        )
+        await interaction.response.send_message(embed=embed)

-    async def colorchat(
-        self,
-        interaction: discord.Interaction,
-        color: str,
-        content: str
-    ):
+    async def colorchat(
+        self,
+        interaction: discord.Interaction,
+        color: str,
+        content: str
+    ):
+        # 색상 파싱
+        try:
+            c = int(color.lstrip("#"), 16)
+        except ValueError:
+            return await interaction.response.send_message(
+                "❌ 유효한 색상 코드를 입력하세요. ex) #FF69B4",
+                ephemeral=True
+            )
+        # Embed 생성
+        embed = discord.Embed(
+            description=content,
+            color=discord.Color(c)
+        )
+        await interaction.response.send_message(embed=embed)

-    async def announce_prefix(self, ctx, color: str, title: str, *, content: str):
+    async def announce_prefix(self, ctx, color: str, title: str, *, content: str):
+        # 색상 파싱
+        try:
+            c = int(color.lstrip("#"), 16)
+        except ValueError:
+            return await ctx.send("❌ 유효한 색상 코드를 입력하세요. ex) #FF69B4")
+        embed = discord.Embed(
+            title=f"{title} /",
+            description=content,
+            color=discord.Color(c)
+        )
+        await ctx.send(embed=embed)
