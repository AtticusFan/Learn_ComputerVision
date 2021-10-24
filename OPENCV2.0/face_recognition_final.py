import face_module as m 

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'
key = 'f85d4cd78eda46cab8549149ac0d146a'                             # 金鑰
gid = 'gp01'                                                         # 群組 Id
#pid = '893f6049-c9b5-463d-87ab-d14c52bbfe0a'                        # 成員 Id

m.face_init(base, key)
m.face_use(gid, ' ') 
#m.face_use(gid, pid)
#m.face_shot('add')                                                  # 新增成員臉部資料
m.face_shot('who')   