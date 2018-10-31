import  requests
from time import *
from random import randint
import random
for i in range(10000):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'close',
            'Host': 'www.wjx.cn',
            'Origin': 'https://www.wjx.cn',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'X-Forwarded-For': str(randint(1, 255))+'.'+str(randint(1, 255))+'.'+str(randint(1, 255))+'.'+str(randint(1, 255)),
            'Referer': 'https://www.wjx.cn/jq/29783542.aspx',
            'Cookie': 'acw_tc=707c9fdd15404654538376839e470618822f1f4552badb67ca168de9c542ca; .ASPXANONYMOUS=ftyYU-Si1AEkAAAAN2Y2MTdiN2QtM2Y5OC00NmQ0LTk0NmQtMzkzMDdlNjJjNzJlAxQMHSIlGt7NCqcXA3fIhtenwd41; UM_distinctid=166aae598601-0f64b4fead3e99-b79193d-1fa400-166aae598623f1; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1540465466,1540468886; ASP.NET_SessionId=ajbmtcptjzlb1i3meh5r0wtb; CNZZDATA4478442=cnzz_eid%3D1307589479-1540461033-%26ntime%3D1540479677; jac29518091=00267952; _uab_collina=154048083923225833918737; WjxUser=UserName=yxy867675930&Type=1; SojumpSurvey=01029B996BA78D3AD608FE9B397D2EAF3AD608000C79007800790038003600370036003700350039003300300000012F00FF5A62BDD57256D8DF06AEE6569AEF0ADD76C6E3D3; lllogcook=1; LastCheckUpdateDate=1; LastCheckDesign=1; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1540481651545; LastActivityJoin=29518091,102004338178; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1540483167'

        }
        data = 'submitdata=1$%s}2$%s' % (randint(1, 2), randint(1, 2))
        url = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=29783542&t=1540483188065&starttime=2018%2F10%2F25%2023%3A59%3A26&rn=3529822698&hlv=1&ktimes=40&jqnonce=87b8f6c1-e1cf-44e8-bfbe-e7e7063cb228&jqsign=%10%1FJ%10N%1EK%19%05M%19KN%05%1C%1CM%10%05JNJM%05M%1FM%1F%18%1E%1BKJ%1A%1A%10 HTTP/1.1'
        url1 = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=29783542&t=1540522345193&nc_csessionid=0192LNBmKlCXyECTYDZr1cmfoRpqay7E4P1IfFmDCrV82zjzYvzQeu9DjrldewD4vkOvJJFS1oT435_Y_-7iFjlhzdKrZpuu-k5NtKF8LCtVga1oCXWYXlMtx3tFOOaQ8m&nc_sig=05a1C7nT4bR5hcbZlAujcdyUKvCCpG6Voy3bfqRb8a6kqGggWyA8OUO7-2ccIVHtXrTcRDNTJuYVlCQfdQOa83DHLbUzWuzeF3iHQR0RW-_GmRCWwBYb5cknzIkUMuZdsK30mqdP3j5pn_N3i9f5zMcL5gLkQML7t8tj31QV8JROhlmHiBhzpU5WfpLm37aGqn1nsacOxEmPqreYk0n9Li8GuHBJ2TYq2Z4uprqp31hbsisaRqe_ZhFNRP_r9kNz7JwXWfjuEMD16lTgFU6q7bBCJyXC9_UWdL1ZNxt8EuzUpWJ3_VaMa7kP3qXaUkOIpWl26zCrdpwEfenuKy1bMrJA&nc_token=1540522332544%3A0.1074149731040186&nc_scene=ic_activity&validate_text=geet&starttime=2018%2F10%2F26%2010%3A52%3A12&rn=3529822698&hlv=1&sd=http%3a%2f%2fwww.wjx.cn%2f&ktimes=22&jqnonce=1ca38121-4dac-4569-8502-f45e87bd4d1c&jqsign=%27uw%25.%27%24%27%3B%22rwu%3B%22%23%20%2F%3B.%23%26%24%3Bp%22%23s.!tr%22r%27u HTTP/1.1'
        url2 = 'https://www.wjx.cn/joinnew/processjq.ashx?submittype=1&curID=29783542&t=1540522622140&nc_csessionid=01K7zDEhI4L1CWGlywDcZNuH4Cf27vSJlKV7_ntrjd6wXDApiR4JLuaHyVxqLdiTq89WPoSCq1QAIaf7UWaIIX_RzdKrZpuu-k5NtKF8LCtVga1oCXWYXlMtx3tFOOaQ8m&nc_sig=05a1C7nT4bR5hcbZlAujcdyaifRdIFvmUAUXuPFww_EY4Ca2-loR1utJa72uDt2EaF-vJ7lE-laUAb_5qMA0L4Ezj-KQj-yi_bQeeBWPnJ_5-NkBe8Ux2dS7LSSaBBggm1oYiK_anT6Bk53TvDJhWgWATEpThDW_KeLnODrd6SLzAlYVXtjxuoZAxinEmke1zGrHGpBtp-6bA_W-pKP3m-LmuHBJ2TYq2Z4uprqp31hbuWaAlp1L59rpIa6lEW3bzO55YytpF1g4chkFG9rFJdjKGwVdOjmVuaaskknNXcEB-Nx5fFAB0XjoWA13VEht0sTqEMIFMHuE8SJnYQczOJ5Q&nc_token=1540522609440%3A0.3478882894082518&nc_scene=ic_activity&validate_text=geet&starttime=2018%2F10%2F26%2010%3A56%3A48&rn=3529822698&hlv=1&sd=http%3a%2f%2fwww.wjx.cn%2f&ktimes=14&jqnonce=6354c484-4f80-4954-a9a7-fa8ae5823cc0&jqsign=8%3D%3B%3Am%3A6%3A%23%3Ah6%3E%23%3A7%3B%3A%23o7o9%23ho6ok%3B6%3C%3Dmm%3E HTTP/1.1'
        r = requests.post(url, data, headers=headers)
        r = requests.post(url1, data, headers=headers)

        print('Using IP:'+headers['X-Forwarded-For']+'提交成功'+r.text)

