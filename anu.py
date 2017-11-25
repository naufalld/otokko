# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re
import requests
from bs4 import BeautifulSoup

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

#ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""                          L͠D̨ ̧͟͞T̛E̶4͢M͏
                       --------------------
「
  「Bantuan LD Bots :」
  ↳ 
    » [нelp0] = Base Command
    » [нelp1] = Settings Command
    » [нelp2] = Mod Command
    » [нelp3] = Group Command
    » [нelp4] = Use For Kicker Command

  「Info Bots :」
  ↳ 
    » Based on : LIN3-TCR
    » Support By : L͠D̨ ̧͟͞T̛E̶4͢M͏
    » Author Bot : Alfathdirk
    » Modding By : • Bama Septituta
	                              • Ervan R.F
    » Version Mod : 1.0.5alpha
    » Type「changelog」
       To See Changelog On v1.0.5alpha
    » Type「supporter」
       To See Supporter On Bots               」
                      --------------------
                          L͠D̨ ̧͟͞T̛E̶4͢M͏"""

helpMessage1 ="""                          L͠D̨ ̧͟͞T̛E̶4͢M͏
                       --------------------
「
  「Basic Command :」
  ↳
    » [id]
    » [mid]
    » [me]
    » [TL:「Text」]
    » [Mc 「mid」]
    » [Gcancel:「Number of people」]
    » [cancelall]
    » [Message change:「text」]
    » [Message check]
    » [Confirm]                      」
                      --------------------
                          L͠D̨ ̧͟͞T̛E̶4͢M͏"""

helpMessage2 ="""                          L͠D̨ ̧͟͞T̛E̶4͢M͏
                       --------------------
「
  「Settings Command :」
  ↳
    » [Contact:「on/off」]
    » [Join:「on/off」]
    » [Leave:「on/off」]
    » [Add:「on/off」]
    » [Share:「on/off」]
                      --------------------
                          L͠D̨ ̧͟͞T̛E̶4͢M͏"""

helpMessage3 ="""                          L͠D̨ ̧͟͞T̛E̶4͢M͏
                       --------------------
「
  「Mod Command :」
  ↳
    » [Steal dp (@)]
    » [Steal home (@)]
    » [speed]
    » [$set]
    » [$read]
                      --------------------
                          L͠D̨ ̧͟͞T̛E̶4͢M͏"""

helpMessage4 ="""                          L͠D̨ ̧͟͞T̛E̶4͢M͏
                       --------------------
「
  「Group Command :」
  ↳
    » [Curl]
    » [Ourl]
    » [url]
    » [url:「Group ID」]
    » [Invite：「mid」]
    » [Kick：「mid」]
    » [Ginfo]
    » [jointicket]
    » [Cancel]
    » [Gn 「group name」]
    » [Nk 「name」]
                      --------------------
                          L͠D̨ ̧͟͞T̛E̶4͢M͏"""

helpMessage5 ="""                          L͠D̨ ̧͟͞T̛E̶4͢M͏
                       --------------------
「Use For Kicker Command :」
↳
  » [Bye]
  » [Kill ban]
  » [Kill 「@」]
  » [Ban 「@」] By Tag
  » [Unban 「@」] By Tag
  » [Ban] Share Contact
  » [Unban] Share Contact
  » [Banlist]
  » [Cek ban]
  » [Cv invite:「mid」]
  » [Cv rename:「name」]
  » [Cv gift]
  » [Respon]
  » [Bot cancel]
  » [Title:]
                      --------------------
                          L͠D̨ ̧͟͞T̛E̶4͢M͏"""

helpMessage6 ="""                          L͠D̨ ̧͟͞T̛E̶4͢M͏
                       --------------------
「Changelog :」

- v1.0.1alpha
• Fixing Bugs
• Delete Unusable Code
• Renew All Command
• Remake Bot Into Selfbot

- v1.0.2alpha
• Added See Group Invitation
• Added See List Group

- v1.0.3alpha
• Added Tag All Members

- v1.0.4alpha
• Fixing Command Clean All Members

- v1.0.5alpha
• Fixing Command Tag All Members
                      --------------------
                          L͠D̨ ̧͟͞T̛E̶4͢M͏"""

helpMessage7 ="""                          L͠D̨ ̧͟͞T̛E̶4͢M͏
                       --------------------
「Supporter :」
- Fazar Riansyah
- Caca

Thanks For Your Support And Your Script :)
                      --------------------
                          L͠D̨ ̧͟͞T̛E̶4͢M͏"""

KAC=[cl]
mid = cl.getProfile().mid
Amid = cl.getProfile().mid
Bmid = cl.getProfile().mid
Cmid = cl.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["u12c5cf853784842cd2e4354e91e66804"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False,
    "tag":True,
    "simsimi":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = cl.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 16:
            ginfo = cl.getGroup(op.param1)    
            cl.sendText(op.param1, "Hi, thx for invited me to " + ginfo.creator.displayName + "'s Groups, Don't Kick Me Out From Group")
            print "\nBOT JOIN THE GROUP\n"

        if op.type == 17:
        	ginfo = cl.getGroup(op.param1)
    		try:
        		sendMessage(op.param1,"Hi, " + cl.getContact(op.param2).displayName + "\nSelamat Datang Di Grup :\n=> " + str(ginfo.name) + "\nOwner Grup Kami Adalah :\n=> " + str(ginfo.creator.displayName))
    		except Exception as e:
        		print e
        		print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        		return

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Already In Banlist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Done ")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Success Delete From Blacklist")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It Is Not in Blacklist")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already In Banlist")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Success Delete From Blacklist")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It Is Not in Blacklist")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[Nama Profil]:\n" + msg.contentMetadata["displayName"] + "\n\n[Id Profil]:\n" + msg.contentMetadata["mid"] + "\n\n[Pesan Status]:\n" + contact.statusMessage + "\n\n[Foto Profil]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Foto Cover]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[Nama Profil]:\n" + contact.displayName + "\n\n[Id Profil]:\n" + msg.contentMetadata["mid"] + "\n\n[Pesan Status]:\n" + contact.statusMessage + "\n\n[Foto Profil]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Foto Cover]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "URL :\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL :\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return

#-----------------------------------Changelog-----------------------------------
	    elif msg.text.lower() == 'changelog':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage6)
                else:
                    cl.sendText(msg.to,helpMessage6)
	    elif msg.text.lower() == 'supporter':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage7)
                else:
                    cl.sendText(msg.to,helpMessage7)
#-----------------------------------Changelog-----------------------------------
#-----------------------------------Help Command-----------------------------------
	    elif msg.text.lower() == 'showcmd':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
	    elif msg.text.lower() == 'help0':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage1)
                else:
                    cl.sendText(msg.to,helpMessage1)
	    elif msg.text.lower() == 'help1':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage2)
                else:
                    cl.sendText(msg.to,helpMessage2)
	    elif msg.text.lower() == 'help2':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage3)
                else:
                    cl.sendText(msg.to,helpMessage3)
	    elif msg.text.lower() == 'help3':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage4)
                else:
                    cl.sendText(msg.to,helpMessage4)
	    elif msg.text.lower() == 'help4':
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage5)
                else:
                    cl.sendText(msg.to,helpMessage5)
#-----------------------------------Help Command-----------------------------------            
            elif ("cgn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("cgn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"Error, Please Retype Correctly!")
            elif "kmid " in msg.text:
                midd = msg.text.replace("kmid ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "invmid " in msg.text:
                midd = msg.text.replace("invmid ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Error, Please Retype Correctly!")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["ourl","link on"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already Open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl","Link off"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "Diblokir"
                        else:
                            u = "Dibuka"
                        cl.sendText(msg.to,"[Nama Grup]:\n" + str(ginfo.name) + "\n\n[Id Grup]:\n" + msg.to + "\n\b[Pembuat Grup]:\n" + gCreator + "\n\n[Gambar Grup]:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nKode Url : " + u + "\nJumlah Member : " + str(len(ginfo.members)) + " Orang\nUndangan Yang Belum Diterima : " + sinvitee + " Orang")
                    else:
                        cl.sendText(msg.to,"[Nama Grup]:\n" + str(ginfo.name) + "\n\n[Id Grup]:\n" + msg.to + "\n\b[Pembuat Grup]:\n" + gCreator + "\n\n[Gambar Grup]:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "id" == msg.text:
                cl.sendText(msg.to,msg.to)
#-------------------------------------Group-------------------------------------
	    elif "seeinv" in msg.text:
                gr = cl.getGroupIdsInvited()
                inv = ""
                for grp in gr:
                    inv += "=> %s  \n" % (cl.getGroup(grp).name)
                cl.sendText(msg.to, "Pending Group :\n\n"+ inv +"\nTotal Pending Group :" +"["+str(len(gr))+"]")
	    elif "seelist" in msg.text:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "=> %s  \n" % (cl.getGroup(i).name + " | Members : [" + str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to, "List Group :\n\n"+ h +"\nTotal Group : " +"["+str(len(gid))+"]")
#-------------------------------------Group-------------------------------------
            elif msg.text in ["wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["hehehe"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["sedih"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["you"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["hmmm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["rename:"]:
                string = msg.text.replace("rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = cl.getProfile()
                    profile_B.displayName = string
                    cl.updateProfile(profile_B)
                    cl.sendText(msg.to,"Change name into " + string + " done")
            elif msg.text in ["sc "]:
                mmid = msg.text.replace("sc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ³","k on","Contact:on","é¡¯ç¤ºï¼šé–‹"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","k off","Contact:off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Contact Set Off")
                    else:
                        cl.sendText(msg.to,"Already On")
	    elif msg.text in ["Tag on","Tag:on"]:
	        if wait["tag"] == True:
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Tag Set On")
		    else:
			cl.sendText(msg.to,"Already On")
		else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
	    elif msg.text in ["Tag off","Tag:off"]:
	        if wait["tag"] == False:
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Tag Set Off")
		    else:
			cl.sendText(msg.to,"Already Off")
		else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
	    elif msg.text in ["Simi on","Simi:on"]:
	        if wait["simsimi"] == True:
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Simi Set On")
		    else:
			cl.sendText(msg.to,"Already On")
		else:
                    wait["simsimi"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Simi Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
	    elif msg.text in ["Simi off","Simi:off"]:
	        if wait["simsimi"] == False:
		    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Simi Set Off")
		    else:
			cl.sendText(msg.to,"Already Off")
		else:
                    wait["simsimi"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Simi Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
            elif msg.text in ["gcancel:"]:
                try:
                    strnum = msg.text.replace("gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Set Off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set"]:
            	group = cl.getGroup(msg.to)
                md = ""
                if wait["contact"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Contact : Active\n"
                else: md+="􀜁􀇍Cyberpunk Girl􏿿 Contact : Not Active\n"
                if wait["autoJoin"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Auto join : Active\n"
                else: md +="􀜁􀇍Cyberpunk Girl􏿿 Auto join : Not Active\n"
                if wait["autoCancel"]["on"] == True:md+="􀜁􀇍Cyberpunk Girl􏿿 Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "􀜁􀇍Cyberpunk Girl􏿿 Group cancel : Not Active\n"
                if group.preventJoinByTicket == False:md+="􀜁􀇍Cyberpunk Girl􏿿 Url : Active\n"
                else: md+="􀜁􀇍Cyberpunk Girl􏿿 Url : Not Active\n"
                if wait["leaveRoom"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Auto leave : Active\n"
                else: md+="􀜁􀇍Cyberpunk Girl􏿿 Auto leave : Not Active\n"
                if wait["timeline"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Share : Active\n"
                else:md+="􀜁􀇍Cyberpunk Girl􏿿 Share : Not Active\n"
                if wait["autoAdd"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Auto add : Active\n"
                else:md+="􀜁􀇍Cyberpunk Girl􏿿 Auto add : Not Active\n"
                if wait["commentOn"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Comment : Active\n"
                else:md+="􀜁􀇍Cyberpunk Girl􏿿 Comment : Not Active\n"
                if wait["atjointicket"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Auto Join Group by Ticket : Active\n"
                else:md+="􀜁􀇍Cyberpunk Girl􏿿 Auto Join Group by Ticket : Not Active\n"
		if wait["tag"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Tag : Active\n"
                else: md +="􀜁􀇍Cyberpunk Girl􏿿 Tag : Not Active\n"
		if wait["simsimi"] == True: md+="􀜁􀇍Cyberpunk Girl􏿿 Simi : Active\n"
                else: md +="􀜁􀇍Cyberpunk Girl􏿿 Simi : Not Active\n"
                cl.sendText(msg.to,"◤Settings◢\n\n" + md + "\nSupport By : L͠D̨ ̧͟͞T̛E̶4͢M͏")
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id","ç¾¤çµ„å…¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["cancelginv"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeâ†’" in msg.text:
                gid = msg.text.replace("album removeâ†’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Add Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Add Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"Message Changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Message Changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Message Change To\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Message Changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Set On")
                    else:
                        cl.sendText(msg.to,"Already On")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","Comment:off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Set Off")
                    else:
                        cl.sendText(msg.to,"Already Off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"Message Changed To\n\n" + str(wait["comment"]))
            elif msg.text in ["gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Add To Comment BL")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"WL To Comment BL")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    anu = "- " + mc
                    cl.sendText(msg.to,anu)
            elif msg.text in ["Spam "]:
                anu = msg.text.replace("Spam ", "")
                anu2 = anu.rstrip('')
                spam = anu2 * 30
                cl.sendText(msg.to,spam)
            elif msg.text == "$set":
                    cl.sendText(msg.to, "Check sider")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "$read":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "People who readed %s\nthat's it\n\nPeople who have ignored reads\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
#-----------------------------------------------
            elif msg.text in ["Leave"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Kill"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Cleanse" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Cleanse","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Just some casual cleansing ô")
                    cl.sendText(msg.to,"Group cleansed.")
                    cl.sendText(msg.to,"Fuck You All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg.to,"Group cleanse")
            elif "vtag " in msg.text:
                  if msg.from_ in admin:
                       nk0 = msg.text.replace("vtag ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"User Doesn't Exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl,ki,kk,kc]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"User Has Been Kick Out From Group")
            elif "Blacklist @" in msg.text:
                _name = msg.text.replace("Blacklist @","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Contact Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Blacklist Success")
                                except:
                                    cl.sendText(msg.to,"Error")
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact Not found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Ban Success")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Unban Success")
                            except:
                                cl.sendText(msg.to,"Unban Success")
#-----------------------------------------------
            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				cl.sendText(msg.to,(bctxt))
#-----------------------------------------------

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------		
	    elif msg.text in ["Mention","mention","Tag","tag"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
		anu = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
		for nganu in anu:
		    anu += "[-] " + msg
                try:
                    cl.sendMessage(msg.to,"◤Mention◢\n" + nganu)
                except Exception as error:
                    print error
#------------------------------------------------------------------	
            elif "Steal home @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"			
#------------------------------------------------------------------
            elif "Steal dp @" in msg.text:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"	
#------------------------------------------------------------------
            elif "Info @" in msg.text:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                van = cl.getGroup(msg.to)
                for linedev in van.members:
                    if target == linedev.displayName:
                        mid = cl.getContact(linedev.mid)
                        #./linedev/ervan
                        try:
                            cover = cl.channel.getCover(linedev.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + mid.displayName + "\n[Mid]:\n" + linedev.mid + "\n[BIO]:\n" + mid.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + mid.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
            elif "Info2 " in msg.text:
                mid = msg.text.replace("Info2 ","")
                anu = cl.getContact(mid)
                try:
                    cover = cl.channel.getCover(mid)
                except:
                    cover = ""
                cl.sendText(msg.to,"[Display Name]:\n" + anu.displayName + "\n[Mid]:\n" + mid + "\n[BIO]:\n" + anu.statusMessage + "\n[Ava]:\nhttp://dl.profile.line-cdn.net/" + anu.pictureStatus + "\n[Cover]:\n" + str(cover))
#------------------------------------------------------------------
	    elif "Bokep " in msg.text:
	        bkp = msg.text.replace("Bokep ", "")
	        anu = bkp.rstrip(' ')
	        path = "http://xvideos.com/?k=" + anu
	        path2 = "http://xhamster.com/search?q=" + anu
	        cl.sendText(msg.to,"Best Result...")
	        cl.sendText(msg.to,path)
	        cl.sendText(msg.to,path2)
	    elif "Google " in msg.text:
	        ggl = msg.text.replace("Google ", "")
       	        anu = ggl.rstrip(' ')
    	        path = "http://google.com/search?q=" + anu
	    	cl.sendText(msg.to,"Best Result...")
		cl.sendText(msg.to,path)
            elif "Youtube " in msg.text:
		yt = msg.text.replace("Youtube ", "")
                anu = yt.rstrip(' ')
		path = "https://www.youtube.com/results?search_query=" + anu
		cl.sendText(msg.to,"Result...")
		cl.sendText(msg.to,path)
#------------------------------------------------------------------
	    elif "bio " in msg.text:
                nk0 = msg.text.replace("bio ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                    cl.sendText(msg.to,"user does not exist")
                    pass
                else:
                    for target in targets:
                       try:
                           contact = cl.getContact(target)
                           y = contact.statusMessage
                           cl.sendText(msg.to,"Status Message:\n" + y)
                       except Exception as e:
                           cl.sendText(msg.to,"Error")
                           print e
	    elif "mid @" in msg.text:
                _name = msg.text.replace("mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#------------------------------------------------------------------		    
	    elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh =int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
            if txt[1] == "on":
                if jmlh <= 60000000:
                    for x in range(jmlh):
                        cl.sendText(msg.to, teks)
                else:
                    cl.sendText(msg.to, "Out off range")
            elif txt[1] == "off":
                if jmlh <= 60000000:
                    cl.sendText(msg.to, tulisan)
                else:
                    cl.sendText(msg.to, "Out off range")
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Nothing In Banlist")
                else:
                    cl.sendText(msg.to,"Wait......")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"----------Blacklist user----------\n" + mc + "----------Blacklist user----------")
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["kban"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["clear"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")	
            
            elif ("Bye " in msg.text):
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        cl.kickoutFromGroup(msg.to,[target])
                    except:
                        pass
				
            elif "albumâ†’" in msg.text:
                try:
                    albumtags = msg.text.replace("albumâ†’","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecâ†’" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecâ†’","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
	if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
