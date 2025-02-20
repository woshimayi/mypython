'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: xml_to_c.py
@time: 2024/09/19 14:23
@desc: xml 生成 c 代码
'''

import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

types = {'boolean': 'eCWMP_tBOOLEAN', 'int': 'eCWMP_tINT', 'string': 'eCWMP_tSTRING', 'unsignedInt': 'eCWMP_tUINT',
         'object': 'eCWMP_tOBJECT'}

flags = {"ReadWrite": "CWMP_WRITE|CWMP_READ", "hideParameterFromAcs": "CWMP_HIDDEN",
         "isTr69Password": "CWMP_ISPASSWORD", 'ReadOnly': "CWMP_READ"}

struct_types = {'boolean': 'uword8', 'string': 'word8', 'unsignedInt': 'uword32', 'int': 'word32'}

dup_types = {'boolean': 'booldup', 'string': 'strdup', 'unsignedInt': 'uintdup', 'int': 'intdup'}

xml_type = {'boolean': 'XML_ENTRY_PRIMITIVE2', 'unsignedInt': 'XML_ENTRY_PRIMITIVE2', 'int': 'XML_ENTRY_PRIMITIVE2',
            'string': 'XML_ENTRY_STRING2'}


class GenerateObject(object):
    """docstring for GenerateObject"""

    def __init__(self):
        super(GenerateObject, self).__init__()
        self.fw = ''
        self.enums = []
        self.ObjDict = []
        self.ObjCWMP_PRMT = ''
        self.CWMP_OP = ''
        self.CWMP_LEAF = ''
        self.CWMP_LINKNODE = ''
        self.getfun = ''
        self.setfun = ""

        # mul node
        self.Objfun = ""

        self.headfile = False

        self.struct = ''
        self.igd_tab = ''
        self.oid = ''
        self.strAdd = ''
        self.strDel = ''
        self.strSet = ''
        self.strGet = ''
        self.strgetNUm = ''
        self.strGetAllNum = ''
        self.strGetAllInfo = ''
        self.strInit = ''

    def headObj(self, objName, name, oid):
        ObjCWMP_OP = 't' + objName + 'LeafOP'
        ObjCWMP_PRMT = 't' + objName + 'LeafInfo'
        self.ObjshortObjectName = objName
        self.struct = 'Igd' + objName + 'Tab'

        self.igd_tab = ("IGD_%s_TAB" % (objName.upper()))
        self.oid = oid
        self.enums = []

        self.fw = open("prmt_" + objName + '.c', 'w')

        if not self.headfile:
            self.headfile = True
            # self.fw.write("#include " + '"prmt_' + objName + '.h"\n')
            self.fw.write('''#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"\n''')

            self.fw.write("/*" + name + '*/\n')

        self.Objfun = 'Obj' + objName

        self.fw.write('\n\nstruct CWMP_OP ' + ObjCWMP_OP + ' = { NULL ,' + self.Objfun + '};\n')
        #         self.fw.write('struct CWMP_PRMT t' + objName + '[] = \n{\n')
        #         self.fw.write('''\t/*(name,			type,		flag,			op)*/
        # \t{"%s", eCWMP_tOBJECT, CWMP_READ | CWMP_WRITE, &%s, (void *)& gArea_Cmcc_Common},\n''' % (objName, ObjCWMP_OP))
        #         self.fw.write('}\n')

        # self.fw.write('enum e%sLeaf\n' % (objName))
        # self.fw.write('{\n')
        # self.fw.write('\te%s,\n' % objName)
        # self.fw.write('};\n')

        # CWMP_NODE
        # self.fw.write('struct CWMP_NODE t%sObject[] =\n' % (objName))
        # self.fw.write('{\n')
        # self.fw.write('\t{ &t%s[e%s], NULL, NULL},\n' % (objName, objName))
        # self.fw.write('\t{ NULL, NULL, NULL }\n')
        # self.fw.write('};\n')
        pass

    def headMulObj(self, objDict):
        print('\nheadMulObj', objDict)
        self.fw.close()
        self.headfile = True
        # self.fw.write("#include " + '"prmt_' + objName + '.h"\n')
        self.fw = open('prmt_smart.c', 'w')
        self.fw.write('''#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"\n\n\n''')
        objName = ''
        flag = False

        for obj in objDict:
            print('\nobj ', obj)
            flag = False
            if 'InternetGatewayDevice' in obj or 'X_CMCC_SmartGateway' in obj:
                continue
            for key, val in obj.items():
                print('zzzzzz', key, val)
                if not flag:
                    flag = True
                    print('zzzzzzzzzzzzzzzz', key.split('.'))
                    objName = key.split('.')[-2]
                    self.fw.write('struct CWMP_PRMT t' + key.split('.')[-2] + '[] = \n{\n')
                    self.fw.write('\t/*(name,			type,		flag,			op)*/\n')
                if val:
                    self.fw.write(
                        '\t{"%s", eCWMP_tOBJECT, CWMP_READ | CWMP_WRITE, &t%sLeafOP, (void *)& gArea_Cmcc_Common},\n' % (
                        key, key))
                else:
                    self.fw.write(
                        '\t{"%s", eCWMP_tOBJECT, CWMP_READ | CWMP_WRITE, NULL,        (void *)& gArea_Cmcc_Common},\n' % (
                            key))
            self.fw.write('};\n')

            flag = False
            for key, val in obj.items():
                print('zzzzzz', key, val)
                if not flag:
                    flag = True
                    self.fw.write('enum e%sLeaf\n{\n' % (key))
                self.fw.write('\te%s,\n' % key)
            self.fw.write('};\n\n')

            flag = False
            for key, val in obj.items():
                print('zzzzzz', key, val)
                if not flag:
                    flag = True
                    self.fw.write('struct CWMP_NODE t%sObject[] =\n{\n' % (key))
                if val:
                    self.fw.write('\t{ &t%s[e%s], NULL, NULL},\n' % (objName, key))
                else:
                    self.fw.write('\t{ &t%s[e%s], NULL, NULL},\n' % (objName, key))
            self.fw.write('\t{ NULL, NULL, NULL }\n')
            self.fw.write('};\n\n')

        self.fw.close()
        pass

    def headLink(self, name, shortObjectName):
        l_ObjCWMP_PRMT = 't' + shortObjectName + 'ObjInfo'
        # self.ObjshortObjectName = shortObjectName

        # self.fw = open("prmt_" + shortObjectName + '.c', 'a+')
        if not self.headfile:
            self.headfile = True
            self.fw.write("#include" + '"prmt_' + shortObjectName + '.h"\n')
            self.fw.write("/*" + name + '*/\n')

        self.fw.write('struct CWMP_PRMT ' + l_ObjCWMP_PRMT + '[] =\n{\n')

        str = "\t{\"0\",  eCWMP_tOBJECT,  CWMP_READ | CWMP_WRITE | CWMP_LNKLIST,  NULL, (void *)& gArea_Cmcc_Common}\n};\n"
        self.fw.write(str)

        self.fw.write('enum e%sLeaf\n' % (shortObjectName))
        self.fw.write('{\n')
        self.fw.write('\te%s,\n' % shortObjectName)
        self.fw.write('};\n')

        # CWMP_LINKNODE
        self.CWMP_LINKNODE = 't%sObject' % (shortObjectName)
        self.fw.write('struct CWMP_LINKNODE %s[] =\n' % (self.CWMP_LINKNODE))
        self.fw.write('{\n')
        self.fw.write(
            '\t{ &%s[e%s],  %s,  NULL,       NULL,           0},\n' % (l_ObjCWMP_PRMT, shortObjectName, self.CWMP_LEAF))
        self.fw.write('\t{ NULL }\n')
        self.fw.write('};\n')

        pass

    def head(self, name, shortObjectName):
        self.CWMP_OP = 't' + shortObjectName + 'LeafOP'
        self.ObjCWMP_PRMT = 't' + shortObjectName + 'LeafInfo'
        self.shortObjectName = shortObjectName
        self.enums = []
        self.ObjshortObjectName = shortObjectName
        self.struct = 'Igd' + shortObjectName + 'Tab'
        self.igd_tab = ("IGD_%s_TAB" % (shortObjectName.upper()))

        self.getfun = 'get' + shortObjectName
        self.setfun = 'set' + shortObjectName

        if not self.headfile:
            self.fw = open("prmt_" + objName + '.c', 'w')
            self.headfile = True
            self.fw.write('''
#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"

''')
            self.fw.write("#include" + ' "prmt_' + shortObjectName + '.h"\n')
            self.fw.write("/*" + name + '*/\n')

        self.fw.write('\n\nstruct CWMP_OP ' + self.CWMP_OP + 'Childen= {' + self.getfun + ',' + self.setfun + '};\n')
        self.fw.write('struct CWMP_PRMT ' + self.ObjCWMP_PRMT + '[] =\n{\n')
        pass

    # def tail(self, name, shortObjectName):
    #     with open("prmt_"+shortObjectName+'.c', 'a+') as fw:

    def body(self, shortObjectName, name, type, flag, dict):
        CWMP_OP = 't' + shortObjectName + 'LeafOP'
        self.enums.append(name)
        self.ObjDict.append(dict)
        str = "\t{\"%s\",  %s, %s,  &%sChilden, (void *)&gArea_Cmcc_Common},\n" % (name, type, flag, CWMP_OP)
        # print('zzzzz', str)
        self.fw.write(str)

    def bodyEnd(self):
        self.fw.write("};\n")

    def GenEnum(self, shortObjectName):
        # enum
        self.fw.write('enum e%sLeaf\n' % (shortObjectName))
        self.fw.write('{\n')
        for enum in self.enums:
            self.fw.write('\te%s%s,\n' % (shortObjectName, enum))
        self.fw.write('};\n')

        # CWMP_LEAF
        self.CWMP_LEAF = 't' + shortObjectName + 'Leaf'
        self.fw.write('struct CWMP_LEAF %s[] =\n' % (self.CWMP_LEAF))
        self.fw.write('{\n')
        for enum in self.enums:
            self.fw.write('\t{&%s[e%s%s]},\n' % (self.ObjCWMP_PRMT, shortObjectName, enum))
        self.fw.write('\t{ NULL }\n')
        self.fw.write('};\n\n\n')

    def getIndexNum(self):
        pass

    def GenMulIndex(self):
        pass

    def GenStruct(self, mulNodeFlag):
        self.fw.close()

        self.fw = open("igdCm" + objName + '.h', 'w')
        self.fw.write('''#ifndef _IGD_CM_%s_PUB_H_
#define _IGD_CM_%s_PUB_H_

#include <igdGlobalTypeDef.h>
#include <igdCmFeatureDef.h>\n\n''' % (shortObjectName.upper(), shortObjectName.upper()))

        self.fw.write("#define IGD_%s_TAB  (IGD_DEVICE_TAB_START + %s)\n" % (shortObjectName.upper(), self.oid))
        self.fw.write("#define %s_MAX 16\n\n\n" % shortObjectName.upper())
        self.fw.write('typedef struct\n')
        self.fw.write('{\n')
        self.fw.write('\tuword32 ulStateAndIndex;\n')
        self.fw.write('\tuword32 ulIndex;\n\n')

        i = 0
        for dict in self.ObjDict:
            # print('3333333', dict)
            if dict['type'] == 'unsignedInt':
                self.fw.write('\t%s %s;\n' % (struct_types[dict['type']], dict['name']))
            elif dict['type'] == 'string':
                self.fw.write('\t%s %s[%s];\n' % (struct_types[dict['type']], dict['name'], dict.get('maxlength')))
            elif dict['type'] == 'boolean':
                self.fw.write('\t%s %s;\n' % (struct_types[dict['type']], dict['name']))

            strname = dict['name']
            self.fw.write('#define %s_ATTR_MASK_BIT%d_%s (1<<%d)\n' % (shortObjectName.upper(), i, strname.upper(), i))
            i = i + 1

        self.fw.write('#define QOS_LIST_ATTR_MASK_ALL (0xfff)\n')
        self.fw.write('\tuword32 ulBitmap;\n')
        self.fw.write('} __PACK__ %s;\n\n\n' % (self.struct))
        print('dict', self.ObjDict)

        self.headFileIgd(mulNodeFlag)

        self.fw.write('#endif\n')

        self.headFilexml()
        pass

    def igdGenfile(self):
        self.fw.close()

        self.fw = self.fw = open("igdCm" + objName + '.c', 'w')
        self.fw.write(
            '''#include "mib.h"
#include "hi_ipc.h"
#include <hi_netapp.h>
#include "hi_uspace.h"
#include "hi_wan.h"
#include "hi_wifi.h"
#include "hi_wifi_msg.h"
#include "hi_wifi_sta.h"
#include "hi_timer.h"
#include "hi_notifier.h"
#include "hi_board.h"
#include <igdCmModulePub.h>

#include "hg_pub_path.h"
#include "hbus_url.h"
#include "hbus_api.h"
#include "hgslog.h"
#include "hgslog_api.h"
#include "hg_region_code.h"

#undef CM_LOG
#define CM_LOG(fmt, args...) hi_debug(HI_SUBMODULE_CM_QOS, "[CM:%s(%d)]" fmt "\\r\\n", __func__, __LINE__, ##args)
#define CM_ERR(fmt, args...) printf("[CM:%s(%d)]" fmt "\\r\\n", __func__, __LINE__, ##args)\n\n
''')

        pass

    def igdAddfun(self, shortObjectName):

        str = '''
{
    word32  totalNum = 0, lInsNum = 0, lIndex = 0;
	word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdFastPathSpeedUpServiceTab currObj;
	IgdFastPathSpeedUpServiceTab entry;
	IgdFastPathSpeedUpServiceTab  *newObj = (IgdFastPathSpeedUpServiceTab *)pucInfo;

	totalNum = mib_chain_total(IGD_FASTPATHSPEEDUPSERVICE_TAB);
	CM_LOG("totalNum = %d", totalNum);

	for (lInsNum = 0; lInsNum < totalNum; lInsNum++)
	{
		HI_OS_MEMSET_S(&entry, sizeof(IgdFastPathSpeedUpServiceTab), 0, sizeof(IgdFastPathSpeedUpServiceTab));
		if (! mib_chain_get(IGD_FASTPATHSPEEDUPSERVICE_TAB, lInsNum, (void *)&entry))
			continue;
		CM_LOG("ulIndex = %d", entry.ulIndex);

		if (entry.ulIndex > lIndex)
			lIndex = entry.ulIndex;
	}

	HI_OS_MEMSET_S(&currObj, sizeof(IgdFastPathSpeedUpServiceTab), 0, sizeof(IgdFastPathSpeedUpServiceTab));
	HI_OS_MEMCPY_S(&entry, sizeof(IgdFastPathSpeedUpServiceTab), newObj, sizeof(IgdFastPathSpeedUpServiceTab));
	entry.ulIndex = lInsNum + 1;
	entry.ulStateAndIndex = 0;
	CM_LOG("ulIndex = %d", entry.ulIndex);
	if (!totalNum)
	{
		currObj.ulIndex = 1;
	}
	CM_LOG("ulIndex = %d", entry.ulIndex);
	if (mib_chain_add(IGD_FASTPATHSPEEDUPSERVICE_TAB, (unsigned char *)&entry))
	{
		/*backfill TaskId*/
		lRet = IGD_CM_OPERATE_SUCCESS;
	}
	newObj->ulIndex = lIndex + 1;
	return lRet;
}
'''
        str1 = str.replace('IgdFastPathSpeedUpServiceTab', self.struct)
        str1 = str1.replace('IGD_FASTPATHSPEEDUPSERVICE_TAB', self.igd_tab)

        self.fw.write('word32 igdCm%sAdd(uword8 *pucInfo, uword32 len)' % (shortObjectName))
        self.fw.write(str1)
        pass

    def igdDelfun(self, shortObjectName):
        str = '''
        {
	word32 i = 0, totalNum = 0;
	IgdQosListAttrConfTab *pcurrObj = (IgdQosListAttrConfTab *)pucInfo;
	IgdQosListAttrConfTab currObj;

	CM_LOG("ulIndex = %d", pcurrObj->ulIndex);

	totalNum = mib_chain_total(IGD_QOS_LIST_TAB);
	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&currObj, sizeof(currObj), 0, sizeof(currObj));
		if (!mib_chain_get(IGD_QOS_LIST_TAB, i, (void *)&currObj))
		{
			continue;
		}
		if (pcurrObj->ulIndex == currObj.ulIndex)
		{
			break;
		}
	}
	CM_LOG("ulStateAndIndex=%d ulIndex = %d not found.\\r\\n", pcurrObj->ulStateAndIndex, pcurrObj->ulIndex);

	if (i >= totalNum)
	{
		CM_LOG("ulStateAndIndex=%d ulIndex = %d  not found.\\r\\n", pcurrObj->ulStateAndIndex, pcurrObj->ulStateAndIndex);
		return IGD_CM_OPERATE_FAIL;
	}

	mib_chain_delete(IGD_QOS_LIST_TAB, i);
	return IGD_CM_OPERATE_SUCCESS;
}\n
'''
        self.fw.write('\nword32 igdCm%sDel(uword8 *pucInfo, uword32 len)' % (shortObjectName))
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)

        pass

    def igdGetfun(self, shortObjectName):
        str = '''
{
	word32 i, totalNum, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdQosListAttrConfTab currObj;
	IgdQosListAttrConfTab *newObj = NULL;

	newObj = (IgdQosListAttrConfTab *)pucInfo;

	CM_LOG("ulIndex=%d \\r\\n", newObj->ulIndex);

	totalNum = mib_chain_total(IGD_QOS_LIST_TAB);
	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&currObj, sizeof(currObj), 0, sizeof(currObj));
		if (!mib_chain_get(IGD_QOS_LIST_TAB, i, (void *)&currObj))
		{
			continue;
		}
		CM_LOG("i=%d ulIndex=%d currObj.ulIndex = %d newObj->ulIndex = %d\\n",  i, currObj.ulIndex, currObj.ulIndex,
		       newObj->ulIndex);

		if (currObj.ulIndex == newObj->ulIndex)
		{
			break;
		}
	}
	if (i >= totalNum)
	{
		CM_LOG("taskId=%d not found.\\r\\n", newObj->ulIndex);
		return IGD_CM_OPERATE_FAIL;
	}

	/*backfill value*/
	HI_OS_MEMCPY_S(newObj, sizeof(*newObj), &currObj, sizeof(IgdQosListAttrConfTab));

	return lRet;
}\n
'''
        self.fw.write('word32 igdCm%sGet(uword8 *pucInfo, uword32 len)' % (shortObjectName))
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)
        pass

    def igdSetfun(self, shortObjectName):
        str = '''
{	
    word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdQosListAttrConfTab currObj;
	IgdQosListAttrConfTab IgdQosListAttrConfTabTmp, *newObjTmp = NULL;
	word32 i, totalNum;

	newObjTmp = &IgdQosListAttrConfTabTmp;
	HI_OS_MEMSET_S(newObjTmp, sizeof(IgdQosListAttrConfTab), 0, sizeof(IgdQosListAttrConfTab));
	HI_OS_MEMCPY_S(newObjTmp, sizeof(*newObjTmp), pucInfo, sizeof(IgdQosListAttrConfTab));
	HI_OS_MEMSET_S(&currObj, sizeof(IgdQosListAttrConfTab), 0, sizeof(IgdQosListAttrConfTab));

	totalNum = mib_chain_total(IGD_QOS_LIST_TAB);
	CM_LOG("totalNum = %d", totalNum);
	for (i = 0; i < totalNum; i++)
	{
		if (!mib_chain_get(IGD_QOS_LIST_TAB, i, (void *)&currObj))
		{
			continue;
		}
		CM_LOG("i=%d ulIndex=%d\\n", i, currObj.ulIndex);

		if (currObj.ulIndex == newObjTmp->ulIndex)
		{
			break;
		}
	}
	if (i == totalNum)
	{
		CM_LOG("task id %d not found.\\r\\n", newObjTmp->ulIndex);
		return IGD_CM_OPERATE_FAIL;
	}

// un todo\n\n
'''

        strEnd = '''
	lRet = mib_chain_update(IGD_QOS_LIST_TAB, (void *)&currObj, i);
	if (!lRet)
	{
		CM_LOG("lRet(%d): mib_chain_update(IGD_QOS_LIST_TAB, (void *)&currObj, 0) failed !!!", lRet);
		return lRet;
	}
	CM_LOG("lRet = %d", lRet);

	return 0;
}
\n'''
        self.fw.write('word32 igdCm%sSet(uword8 *pucInfo, uword32 len)' % (shortObjectName))
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)

        i = 0
        for dict in self.ObjDict:
            bitmap = '%s_ATTR_MASK_BIT%s_%s' % (shortObjectName.upper(), i, dict['name'].upper())
            self.fw.write(
                '''
                if ((newObjTmp->ulBitmap & %s) == %s)
                {
                    %s
                }''' % (bitmap, bitmap, self.setIgdTypeCopy(dict['type'], dict['name'])))
            i = i + 1

        str1 = strEnd.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)
        pass

    def igdSingleGetfun(self, shortObjectName):
        str = '''
{
	word32 lRet;
	IgdQosAttrConfTab entry;
	IgdQosAttrConfTab *currObj = NULL;

	currObj = (IgdQosAttrConfTab *)pucInfo;
	HI_OS_MEMSET_S(&entry, sizeof(IgdQosAttrConfTab), 0, sizeof(IgdQosAttrConfTab));

	if (mib_chain_get(IGD_QOS_TAB, 0, (void *)&entry))
	{
		HI_OS_MEMCPY_S(currObj, sizeof(IgdQosAttrConfTab), &entry, sizeof(IgdQosAttrConfTab));
		lRet = IGD_CM_OPERATE_SUCCESS;
	}
	else
	{
		CM_LOG("mib_chain_get IGD_QOS_TAB is fail.\\t\\n");
		lRet = IGD_CM_OPERATE_FAIL;
	}

	return lRet;
}\n
'''
        self.fw.write('word32 igdCm%sGet(uword8 *pucInfo, uword32 len)' % (shortObjectName))
        str1 = str.replace('IgdQosAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_TAB', self.igd_tab)
        self.fw.write(str1)
        pass

    def igdSingleSetfun(self, shortObjectName):
        str = '''
{
	CM_LOG("*************entry in igdCmSecureMacFilterAttrSet*************\\n");

	IgdQosAttrConfTab currObj;
	IgdQosAttrConfTab *newObjTmp = NULL;

	if (!pucInfo)
		return (IGD_CM_GLOBAL_INPUT_PARA_ERROR);

	newObjTmp = (IgdQosAttrConfTab *)pucInfo;
	HI_OS_MEMSET_S(&currObj, sizeof(IgdQosAttrConfTab), 0, sizeof(IgdQosAttrConfTab));
	if (0 == mib_chain_get(IGD_QOS_TAB, 0, (void *)&currObj))
	{
		CM_LOG("mib_chain_get IGD_QOS_TAB is fail.\\t\\n");
		mib_chain_add(IGD_QOS_TAB, (void *)&currObj);
	}

'''

        strEnd = '''
	mib_chain_update(IGD_QOS_TAB, (void *)&currObj, 0);

	return 0;
}
\n'''
        self.fw.write('word32 igdCm%sSet(uword8 *pucInfo, uword32 len)' % (shortObjectName))
        str1 = str.replace('IgdQosAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_TAB', self.igd_tab)
        self.fw.write(str1)

        i = 0
        for dict in self.ObjDict:
            bitmap = '%s_ATTR_MASK_BIT%s_%s' % (shortObjectName.upper(), i, dict['name'].upper())
            self.fw.write(
                '''
                if ((newObjTmp->ulBitmap & %s) == %s)
                {
                    %s
                }''' % (bitmap, bitmap, self.setIgdTypeCopy(dict['type'], dict['name'])))
            i = i + 1

        str1 = strEnd.replace('IgdQosAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_TAB', self.igd_tab)
        self.fw.write(str1)
        pass

    def igdGetNumfun(self, shortObjectName):
        str = '''
{
	*entrynum = mib_chain_total(IGD_QOS_LIST_TAB);
	CM_LOG("entrynum [%d].\\r\\n", *entrynum);
	return IGD_CM_OPERATE_SUCCESS;
}\n
'''
        self.fw.write('word32 igdCm%sGetNum(uword32 *entrynum)' % (shortObjectName))
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)
        pass

    def igdGetAllNumfun(self, shortObjectName):
        str = '''
{
	uword32 allIndex[IGD_TIMED_TASK_NUM];
	word32 i, j = 0, totalTaskNum;
	IgdQosListAttrConfTab qosEntry;

	totalTaskNum = mib_chain_total(IGD_QOS_LIST_TAB);
	CM_LOG("totalTaskNum  = %d", totalTaskNum);
	for (i = 0; i < totalTaskNum; i++)
	{
		HI_OS_MEMSET_S(&qosEntry, sizeof(qosEntry), 0, sizeof(qosEntry));
		if (!mib_chain_get(IGD_QOS_LIST_TAB, i, (void *)&qosEntry))
		{
			continue;
		}
		allIndex[j] = qosEntry.ulIndex;
		CM_LOG("allIndex[%d] = [%d].\\r\\n", j, allIndex[j]);
		j++;
	}

	HI_OS_MEMCPY_S(pucInfo, (sizeof(uword32)*totalTaskNum), allIndex, (sizeof(uword32)*totalTaskNum));

	return IGD_CM_OPERATE_SUCCESS;
}\n
'''
        self.fw.write('word32 igdCm%sGetAllIndex(uword8 *pucInfo, uword32 len)' % (shortObjectName))
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)
        pass

    def igdGetAllInfofun(self, shortObjectName):
        str = '''
{
	word32 i, j = 0, totalNum, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdQosListAttrConfTab tmpObj;
	IgdQosListAttrConfTab *newObj = NULL;

	newObj = (IgdQosListAttrConfTab *)pucInfo;

	totalNum = mib_chain_total(IGD_QOS_LIST_TAB);
	CM_LOG("totalNum  = %d", totalNum);
	if (0 == totalNum)
	{
		CM_LOG("aosnet timed task is empty !\\r\\n");
		return IGD_CM_OPERATE_FAIL;
	}

	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&tmpObj, sizeof(tmpObj), 0, sizeof(tmpObj));
		if (!mib_chain_get(IGD_QOS_LIST_TAB, i, (void *)&tmpObj))
		{
			continue;
		}
		CM_LOG("ulStateAndIndex = %d ulIndex = %d", tmpObj.ulStateAndIndex, tmpObj.ulIndex);
		HI_OS_MEMCPY_S(&newObj[j], sizeof(IgdQosListAttrConfTab), &tmpObj, sizeof(IgdQosListAttrConfTab));
		j++;
	}

	return lRet;
}\n
'''
        self.fw.write('word32 igdCm%sGetAllInfo(uword8 *pucInfo, uword32 len)' % (shortObjectName))
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)
        pass

    def igdinit(self, shortObjectName):
        str = '''
{
	CM_LOG("############ Timed Task Attribute Table Init Start ############\\n");

	word32 lInsNum = 0, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdQosListAttrConfTab entry;
	IgdQosListAttrConfTab IgdQosListAttrConfTabTmp, *pIgdQosListAttrConfTabTmp = NULL;

	pIgdQosListAttrConfTabTmp = &IgdQosListAttrConfTabTmp;
	HI_OS_MEMSET_S(&entry, sizeof(IgdQosListAttrConfTab), 0, sizeof(IgdQosListAttrConfTab));
	HI_OS_MEMSET_S(pIgdQosListAttrConfTabTmp, sizeof(IgdQosListAttrConfTab), 0, sizeof(IgdQosListAttrConfTab));

	mib_chain_get(IGD_QOS_LIST_TAB, lInsNum, &entry);

	HI_OS_MEMCPY_S(pIgdQosListAttrConfTabTmp, sizeof(*pIgdQosListAttrConfTabTmp), &entry, sizeof(IgdQosListAttrConfTab));

	lRet = igdCmQosAttrSet((uword8 *)pIgdQosListAttrConfTabTmp, sizeof(IgdQosListAttrConfTab));
	if (IGD_CM_OPERATE_SUCCESS != lRet)
	{
		CM_LOG("############ Timed Task Attribute Table Init Failed ############\\n");
	}

	CM_LOG("############  Timed Task Attribute Table Init End ############\\n");

	return lRet;
}\n
        '''
        self.fw.write('word32 igdCm%sInit(void)' % (shortObjectName))
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        str1 = str1.replace('igdCmQosAttrSet', self.strSet)
        self.fw.write(str1)
        pass

    def igdMulInit(self, shortObjectName):
        str = '''
{
	CM_LOG("############ Timed Task Attribute Table Init Start ############\\n");
	word32 lRet = IGD_CM_OPERATE_SUCCESS;

	unsigned int MaxInstNum = 0;
	unsigned int msgLen = 0;
	IgdQosListAttrConfTab *pstParaList = NULL;
	IgdQosListAttrConfTab  entry;

	MaxInstNum = mib_chain_total(IGD_QOS_LIST_TAB);
	if (MaxInstNum == 0) {
		CM_LOG("MAC Filte list table is empty !\\r\\n");
		return IGD_CM_OPERATE_SUCCESS;
	}

	CM_LOG("INIT IGD.X_CMCC_Security.MacFilter.obj	NUM=[%d]\\n", MaxInstNum);
	if (MaxInstNum == 0)
		return 0;
	
	pstParaList = (IgdQosListAttrConfTab *)malloc(MaxInstNum * sizeof(IgdQosListAttrConfTab));
	if (NULL == pstParaList)
		return 0;
	HI_OS_MEMSET_S((char *)pstParaList, MaxInstNum * sizeof(IgdQosListAttrConfTab), 0, MaxInstNum * sizeof(IgdQosListAttrConfTab));
	msgLen = MaxInstNum * sizeof(IgdQosListAttrConfTab);

	lRet = igdCmConfGetAllEntry(IGD_QOS_LIST_TAB,(void *)(pstParaList), msgLen);
	if(lRet != IGD_CM_OPERATE_SUCCESS )
	{
		CM_LOG("[CWMP] GETALL IGD_QOS_LIST_TAB FAIL.(ret:%x)", lRet);
		return -1;
	}
	
	for (int ulloop = 0; ulloop < MaxInstNum; ulloop++)
	{
		if (! mib_chain_get(IGD_QOS_LIST_TAB, ulloop, (void *)&entry))
			continue;

		CM_LOG("INIT INIT InternetGatewayDevice.AhsapiQos.DscpPriority INDEX=[%d]\\n", pstParaList[ulloop].ulIndex);
		lRet = igdCmQosListSet((uword8 *)&entry, sizeof(IgdQosListAttrConfTab));
		if (IGD_CM_OPERATE_SUCCESS != lRet)
		{
			CM_LOG("############ Timed Task Attribute Table Init Failed ############\\n");
		}
	}
	free(pstParaList);

	return lRet;
}\n
'''
        self.fw.write('word32 igdCm%sInit(void)' % (shortObjectName))
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        str1 = str1.replace('igdCmQosListSet', self.strSet)
        self.fw.write(str1)
        pass

    def setfunc(self):
        str = '''
{
	char	*lastname = entity->info->name;
	char	*buf = data;
	unsigned int msgLen = 0;
	IgdQosListAttrConfTab stPara;
	IgdQosListAttrConfTab *pstPara = &stPara;
	unsigned int  instnum = 0;

	if ((name == NULL) || (data == NULL) || (entity == NULL))
		return -1;
	if (entity->info->type != type)
		return ERR_9006;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdQosListAttrConfTab), 0, sizeof(IgdQosListAttrConfTab));
	instnum = getCMCC_InstNum(name);
	if (instnum == 0)
		return ERR_9005;
	pstPara->ulIndex = instnum;
	printf("<%s:%d>Index[%#x]\\n", __FUNCTION__, __LINE__, pstPara->ulIndex);
\n'''

        strEnd = '''
	msgLen = sizeof(stPara);
	CWMP_API_SET_ENTRY_PARA_INFO_FUNC(IGD_QOS_LIST_TAB, (UINT8 *)pstPara, 0, msgLen);
	return 0;
}
\n'''

        self.fw.write("int %s(char *name, struct CWMP_LEAF *entity, int type, void *data)" % self.setfun)
        str1 = str.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)

        i = 0
        for dict in self.ObjDict:
            if i == 0:
                self.fw.write(
                    '''
                    if (!strcmp(lastname, %s[e%s%s].name))
                    {
                        %s
                        pstPara->ulBitmap = %s_ATTR_MASK_BIT%s_%s;
                        %s
                    }''' % (self.ObjCWMP_PRMT, self.shortObjectName, dict['name'],
            self.setTypeValid(dict.get('type'), dict.get('minvalue'), dict.get('maxvalue'), dict.get('maxlength')),
            shortObjectName.upper(), i, dict['name'].upper(), self.setTypeCopy(dict['type'], dict['name'])))
            else:
                self.fw.write(
                    '''else if (!strcmp(lastname, %s[e%s%s].name))
                    {
                        %s
                        pstPara->ulBitmap = %s_ATTR_MASK_BIT%s_%s;
                        %s
                    }
                    ''' % (self.ObjCWMP_PRMT, self.shortObjectName, dict['name'],
           self.setTypeValid(dict.get('type'), dict.get('minvalue'), dict.get('maxvalue'), dict.get('maxlength')),
           shortObjectName.upper(), i, dict['name'].upper(), self.setTypeCopy(dict['type'], dict['name'])))

            i = i + 1

        str2 = strEnd.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str2)
        pass

    def setSingleFunc(self):
        str = '''
{
	char *lastname = entity->info->name;
	char *buf = data;
	IgdQosAttrConfTab stPara;
	IgdQosAttrConfTab *pstPara = &stPara;

	if ((name == NULL) || (data == NULL) || (entity == NULL))
		return -1;
	if (entity->info->type != type)
		return ERR_9006;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdQosAttrConfTab), 0, sizeof(IgdQosAttrConfTab));
\n'''

        strEnd = '''else
	{
		return ERR_9005;
	}

	if (pstPara->ulBitmap)
	{
		CWMP_API_SET_ENTRY_PARA_INFO_FUNC(IGD_QOS_TAB,
		                                  (UINT8 *)pstPara, 0, sizeof(stPara));
	}

	return 0;
}
\n'''

        self.fw.write("int %s(char *name, struct CWMP_LEAF *entity, int type, void *data)" % self.setfun)
        str1 = str.replace('IgdQosAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_TAB', self.igd_tab)

        self.fw.write(str1)

        i = 0
        for dict in self.ObjDict:
            if i == 0:
                self.fw.write(
                    '''
                    if (!strcmp(lastname, %s[e%s%s].name))
                    {
                        %s
                        pstPara->ulBitmap = %s_ATTR_MASK_BIT%s_%s;
                        %s
                    }''' % (self.ObjCWMP_PRMT, self.shortObjectName, dict['name'],
            self.setTypeValid(dict.get('type'), dict.get('minvalue'), dict.get('maxvalue'), dict.get('maxlength')),
            shortObjectName.upper(), i, dict['name'].upper(), self.setTypeCopy(dict['type'], dict['name'])))
            else:
                self.fw.write(
                    '''else if (!strcmp(lastname, %s[e%s%s].name))
                    {
                        %s
                        pstPara->ulBitmap = %s_ATTR_MASK_BIT%s_%s;
                        %s
                    }
                    ''' % (self.ObjCWMP_PRMT, self.shortObjectName, dict['name'],
           self.setTypeValid(dict.get('type'), dict.get('minvalue'), dict.get('maxvalue'), dict.get('maxlength')),
           shortObjectName.upper(), i, dict['name'].upper(), self.setTypeCopy(dict['type'], dict['name'])))

            i = i + 1

        str2 = strEnd.replace('IgdQosAttrConfTab', self.struct)
        str2 = str2.replace('IGD_QOS_TAB', self.igd_tab)
        self.fw.write(str2)
        pass

    def setTypeCopy(self, type, name):
        if type == 'unsignedInt':
            return 'pstPara->%s = *(unsigned int *)buf;' % (name)
        elif type == 'string':
            return 'HI_OS_STRCPY_S(pstPara->%s, sizeof(pstPara->%s), buf);' % (name, name)
        elif type == 'boolean':
            return 'pstPara->%s = *(unsigned int *)buf;' % (name)
        pass

    def setIgdTypeCopy(self, type, name):
        if type == 'unsignedInt':
            return 'currObj.%s = newObjTmp->%s;' % (name, name)
        elif type == 'string':
            return 'HI_OS_MEMCPY_S(currObj.%s, sizeof(currObj.%s), newObjTmp->%s, sizeof(currObj.%s));' % (
            name, name, name, name)
        elif type == 'boolean':
            return 'currObj.%s = newObjTmp->%s;' % (name, name)
        pass

    def setTypeValid(self, type, min, max, maxLen):
        if not min:
            min = '0'
        if not max:
            max = '65535'

        if not maxLen:
            maxLen = '128'

        if type == 'unsignedInt':
            return '''
		int *i = data;
		if (NULL == i)
		{
		    return ERR_9007;
		}
		if (*i < %s || *i > %s )
		{
		    return ERR_9007;
		}\n''' % (min, max)
        elif type == 'string':
            return '''if (strlen(buf) == 0 || NULL == buf || strlen(buf) >= %s) {
			return ERR_9007;
       	}\n''' % (maxLen)
        elif type == 'boolean':
            return '''int *i = data;
		if (i == NULL) {
		    return ERR_9007;
		}
		if (*i < 0 || *i > 1) {
		    return ERR_9007;
		}\n'''
        pass

    def getfunc(self):
        strStart = '''
{
	char	*lastname = entity->info->name;
	unsigned int msgLen = 0;
    unsigned int  instnum = 0;
    
	if ((name == NULL) || (type == NULL) || (data == NULL) || (entity == NULL))
		return -1;

	IgdQosListAttrConfTab stPara;
	IgdQosListAttrConfTab *pstPara = &stPara;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdQosListAttrConfTab), 0, sizeof(IgdQosListAttrConfTab));
	PP("name = %s", name);
	instnum = getCMCC_InstNum(name);
	PP("instnum = %d", instnum);
	if (instnum == 0)
		return ERR_9005;
	pstPara->ulIndex = instnum;

	msgLen = sizeof(stPara);
	pstPara->ulBitmap = QOS_LIST_ATTR_MASK_ALL;
	CWMP_API_GET_ENTRY_PARA_INFO_FUNC(IGD_QOS_LIST_TAB, (UINT8 *)pstPara, 0, msgLen);
	
	*type = entity->info->type;
	*data = NULL;
\n'''

        strEnd = '''else
	{
		return ERR_9005;
	}
	return 0;
}\n       
'''

        self.fw.write("int %s(char *name, struct CWMP_LEAF *entity, int *type, void **data)" % self.getfun)
        str1 = strStart.replace('IgdQosListAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        self.fw.write(str1)

        i = 0
        for dict in self.ObjDict:
            if i == 0:
                self.fw.write('\tif (!strcmp(lastname, %s[e%s%s].name))\n\t{\n\t\t*data = %s(pstPara->%s);\n\t}\n\t' % (
                    self.ObjCWMP_PRMT, self.shortObjectName, dict['name'], self.getType(dict['type']), dict['name']))
            else:
                self.fw.write(
                    'else if (!strcmp(lastname, %s[e%s%s].name))\n\t{\n\t\t*data = %s(pstPara->%s);\n\t}\n\t' % (
                        self.ObjCWMP_PRMT, self.shortObjectName, dict['name'], self.getType(dict['type']),
                        dict['name']))
            i = i + 1

        self.fw.write(strEnd)
        pass

    def getSingleFunc(self):
        strStart = '''
{
	char *lastname = entity->info->name;
	unsigned int msgLen = 0;
	IgdQosAttrConfTab stPara;
	IgdQosAttrConfTab *pstPara = &stPara;

	if ((name == NULL) || (type == NULL) || (data == NULL) || (entity == NULL))
		return -1;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdQosAttrConfTab), 0, sizeof(IgdQosAttrConfTab));

	msgLen = sizeof(stPara);
	pstPara->ulBitmap = QOS_ATTR_MASK_ALL;
	CWMP_API_GET_ENTRY_PARA_INFO_FUNC(IGD_QOS_TAB,
	                                  (UINT8 *)pstPara, 0, msgLen);

	*type = entity->info->type;
	*data = NULL;
\n'''

        strEnd = '''else
	{
		return ERR_9005;
	}
	return 0;
}\n       
'''

        self.fw.write("int %s(char *name, struct CWMP_LEAF *entity, int *type, void **data)" % self.getfun)
        str1 = strStart.replace('IgdQosAttrConfTab', self.struct)
        str1 = str1.replace('IGD_QOS_TAB', self.igd_tab)
        self.fw.write(str1)

        i = 0
        for dict in self.ObjDict:
            if i == 0:
                self.fw.write('\tif (!strcmp(lastname, %s[e%s%s].name))\n\t{\n\t\t*data = %s(pstPara->%s);\n\t}\n\t' % (
                    self.ObjCWMP_PRMT, self.shortObjectName, dict['name'], self.getType(dict['type']), dict['name']))
            else:
                self.fw.write(
                    'else if (!strcmp(lastname, %s[e%s%s].name))\n\t{\n\t\t*data = %s(pstPara->%s);\n\t}\n\t' % (
                        self.ObjCWMP_PRMT, self.shortObjectName, dict['name'], self.getType(dict['type']),
                        dict['name']))
            i = i + 1

        self.fw.write(strEnd)
        pass

    def getType(self, type):
        if type == 'unsignedInt':
            return dup_types[type]
        elif type == 'string':
            return dup_types[type]
        elif type == 'boolean':
            return dup_types[type]

    def ObjGenFunc(self):
        str = '''
{
	struct CWMP_NODE *entity = (struct CWMP_NODE *)e;
	unsigned int ulloop;
	unsigned int msgLen = 0;
	 int ret;
	IgdFastPathSpeedUpServiceTab stPara;
	IgdFastPathSpeedUpServiceTab *pstPara = &stPara;
	IgdFastPathSpeedUpServiceTab *pstParaList = NULL;
	uint32_t *index;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdFastPathSpeedUpServiceTab), 0, sizeof(IgdFastPathSpeedUpServiceTab));
	type = (type == eCWMP_tINITOBJ)?eCWMP_tUPDATEOBJ:type;

	switch( type )
	{
	case eCWMP_tINITOBJ:
		 {
			unsigned int MaxInstNum = 0;
			struct CWMP_LINKNODE **table = (struct CWMP_LINKNODE **)data;

			if( (name==NULL) || (entity==NULL) || (data==NULL) ) return -1;

		  CWMP_API_GET_ENTRY_CNT_FUNC(IGD_FASTPATHSPEEDUPSERVICE_TAB,&MaxInstNum);
		  CWMP_LOG(LOG_DEBUG,"INIT IGD.X_CMCC_Security.UrlFilter.obj  NUM=[%d]\\n",MaxInstNum);
			if(MaxInstNum == 0)
				return 0;

			pstParaList = (IgdFastPathSpeedUpServiceTab *)malloc(MaxInstNum*sizeof(IgdFastPathSpeedUpServiceTab));
			if(NULL == pstParaList) return 0;
			HI_OS_MEMSET_S((UINT8*)pstParaList, MaxInstNum*sizeof(IgdFastPathSpeedUpServiceTab), 0, MaxInstNum*sizeof(IgdFastPathSpeedUpServiceTab));
			msgLen = MaxInstNum*sizeof(IgdFastPathSpeedUpServiceTab);

			CWMP_API_GET_ALL_ENTRY_FUNC(IGD_FASTPATHSPEEDUPSERVICE_TAB,pstParaList,msgLen,free(pstParaList));

			for( ulloop=0; ulloop<MaxInstNum; ulloop++ )
			{
				CWMP_LOG(LOG_DEBUG,"INIT IGD.X_CMCC_Security.UrlFilter.obj	INDEX=[%d]\\n",pstParaList[ulloop].ulIndex);
				if( create_Object(table, tFastPathSpeedUpServiceLINKObject, sizeof(tFastPathSpeedUpServiceLINKObject), 1, pstParaList[ulloop].ulIndex) < 0 )
				{
					 free(pstParaList);
					 return -1;
				}

			}
			//add_objectNum( name, MaxInstNum );
					 free(pstParaList);
			return 0;
		 }
	case eCWMP_tADDOBJ:
		 {
			 if( (name==NULL) || (entity==NULL) || (data==NULL) ) return -1;

			msgLen = sizeof(stPara);
			CWMP_API_ADD_ENTRY_FUNC(IGD_FASTPATHSPEEDUPSERVICE_TAB,pstPara,msgLen);
			CWMP_LOG(LOG_DEBUG,"CM ADD IGD.X_CMCC_Security.UrlFilter.obj  INDEX=[%d]\\n",pstPara->ulIndex);
			*(unsigned int*)data = pstPara->ulIndex;

			 ret = add_Object( name, (struct CWMP_LINKNODE **)&entity->next, tFastPathSpeedUpServiceLINKObject, sizeof(tFastPathSpeedUpServiceLINKObject), data );
			 HI_CWMP_LOG(CM_LOG_INFO_E, 1,"ADD %s .(inst:%d,ret:%x)", name, *(int*)data, ret);

			 return ret;
		 }

	case eCWMP_tDELOBJ:
		{
			pstPara->ulIndex = *(int*)data;
			msgLen = sizeof(stPara);
			CWMP_API_DEL_ENTRY_FUNC(IGD_FASTPATHSPEEDUPSERVICE_TAB,pstPara,msgLen);

			ret = del_Object( name, (struct CWMP_LINKNODE **)&entity->next, *(int*)data );
			 HI_CWMP_LOG(CM_LOG_INFO_E,1, "ADD %s .(inst:%d,ret:%x)", name, *(int*)data, ret);

			return ret;
		}
	case eCWMP_tUPDATEOBJ:
		{
			unsigned int num=0, i, ulIndex = 0;
			struct CWMP_LINKNODE *old_table;

			CWMP_API_GET_ENTRY_CNT_FUNC(IGD_FASTPATHSPEEDUPSERVICE_TAB,&num);

			CWMPDBG( 1, ( stderr, "<%s:%d>[DEBUG]:table_count is %d\\n", __FUNCTION__, __LINE__, num) );
			if(num == 0)
				return 0;

			index = malloc(num * sizeof(uint32_t));
			if(NULL == index) return 0;
			(void)memset_s(index, num*sizeof(uint32_t), 0, num*sizeof(uint32_t));
			msgLen = num * sizeof(uint32_t);
			igdCmConfGetallIndex (IGD_FASTPATHSPEEDUPSERVICE_TAB, (UINT8*)index, msgLen);

			old_table = (struct CWMP_LINKNODE *)entity->next;
			entity->next = NULL;
			for( i=0; i<num;i++ )
			{
				ulIndex = index[i];
				add_Object( name, (struct CWMP_LINKNODE **)&entity->next,  tFastPathSpeedUpServiceLINKObject, sizeof(tFastPathSpeedUpServiceLINKObject), &ulIndex );
			}
			if( old_table )
			{
				destroy_ParameterTable( (struct CWMP_NODE *)old_table );
			}
			free(index);
			return 0;
		}
	}

	return -1;
}\n
'''
        self.fw.write("int %s(char *name, struct CWMP_LEAF *e, int type, void *data)" % self.Objfun)
        str1 = str.replace('IgdFastPathSpeedUpServiceTab', self.struct)
        str1 = str1.replace('IGD_FASTPATHSPEEDUPSERVICE_TAB', self.igd_tab)
        str1 = str1.replace('tFastPathSpeedUpServiceLINKObject', self.CWMP_LINKNODE)
        self.fw.write(str1)

    def headFilePrmt(self, mulNodeFlag):
        self.fw.close()

        self.fw = open("prmt_" + objName + '.h', 'w')
        self.fw.write('''#ifndef _PRMT_%s_HG_H_
#define _PRMT_%s_HG_H_
\n\n''' % (shortObjectName.upper(), shortObjectName.upper()))

        self.CWMP_LEAF = 't' + shortObjectName + 'Leaf'
        self.fw.write('extern struct CWMP_LEAF %s[];\n' % (self.CWMP_LEAF))
        self.fw.write('extern struct CWMP_NODE t%sObject[];\n' % (self.ObjshortObjectName))

        self.fw.write("int %s(char *name, struct CWMP_LEAF *entity, int type, void *data);\n" % self.setfun)
        self.fw.write("int %s(char *name, struct CWMP_LEAF *entity, int *type, void **data);\n" % self.getfun)

        if mulNodeFlag:
            self.fw.write("int %s(char *name, struct CWMP_LEAF *e, int type, void *data);\n\n\n" % self.Objfun)

        self.fw.write('#endif\n')
        pass

    def headFileIgd(self, mulNodeFlag):
        strAdd = 'igdCm%sAdd' % (shortObjectName)
        strDel = 'igdCm%sDel' % (shortObjectName)
        self.strSet = 'igdCm%sSet' % (shortObjectName)
        strGet = 'igdCm%sGet' % (shortObjectName)
        strgetNUm = 'igdCm%sGetNum' % (shortObjectName)
        strGetAllNum = 'igdCm%sGetAllIndex' % (shortObjectName)
        strGetAllInfo = 'igdCm%sGetAllInfo' % (shortObjectName)
        strInit = 'igdCm%sInit' % (shortObjectName)

        if mulNodeFlag:
            self.fw.write('word32 igdCm%sAdd(uword8 *pucInfo, uword32 len);\n' % (shortObjectName))
            self.fw.write('word32 igdCm%sDel(uword8 *pucInfo, uword32 len);\n' % (shortObjectName))

        self.fw.write('word32 igdCm%sGet(uword8 *pucInfo, uword32 len);\n' % (shortObjectName))
        self.fw.write('word32 igdCm%sSet(uword8 *pucInfo, uword32 len);\n' % (shortObjectName))

        if mulNodeFlag:
            self.fw.write('word32 igdCm%sGetNum(uword32 *entrynum);\n' % (shortObjectName))
            self.fw.write('word32 igdCm%sGetAllIndex(uword8 *pucInfo, uword32 len);\n' % (shortObjectName))
            self.fw.write('word32 igdCm%sGetAllInfo(uword8 *pucInfo, uword32 len);\n' % (shortObjectName))

        self.fw.write('word32 igdCm%sInit(void);\n\n\n\n' % (shortObjectName))

        if mulNodeFlag:
            self.fw.write('IGDCM_OPER_REG(%s, %s, %s,%s, %s, %s, %s, %s, 0, 0, 0);\n' % (
            self.igd_tab, strAdd, strDel, self.strSet, strGet, strgetNUm, strGetAllNum, strGetAllInfo))
        else:
            self.fw.write(
                'IGDCM_OPER_REG(%s, 0,  0, %s, %s, 0,  0,  0,  0, 0, 0);\n' % (self.igd_tab, self.strSet, strGet))

        pass

    def headFilexml(self):

        struct_MIB = 'MIB_%s_T' % (self.shortObjectName.upper())
        struct_MIB_1 = 'MIB_%s_Tp' % (self.shortObjectName.upper())
        strTp = 'em_%s_entry' % (self.shortObjectName)

        # self.fw.write('typedef %s %s, *%s;\n' % (self.struct, struct_MIB, struct_MIB_1))

        strStart = '''
MIB_QOS_LIST_Tp *em_qos_list_entry = 0;
XML_DIR_ARRAY( root, em_qos_list_entry, "EM_%s_TAB", 16, IGD_QOS_LIST_TAB);
XML_ENTRY_PRIMITIVE2(em_qos_list_entry, ulStateAndIndex);
XML_ENTRY_PRIMITIVE2(em_qos_list_entry, ulIndex);\n''' % (self.shortObjectName.upper())

        str1 = strStart.replace('MIB_QOS_LIST_Tp', self.struct)
        str1 = str1.replace('IGD_QOS_LIST_TAB', self.igd_tab)
        str1 = str1.replace('em_qos_list_entry', strTp)
        self.fw.write(str1)

        for dict in self.ObjDict:
            self.fw.write('%s(%s, %s);\n' % (self.getXmlType(dict['type']), strTp, dict['name']))

        self.fw.write('XML_ENTRY_PRIMITIVE2(%s, ulBitmap);\n' % (strTp))

    def getXmlType(self, type):
        if type == 'unsignedInt':
            return xml_type[type]
        elif type == 'string':
            return xml_type[type]
        elif type == 'boolean':
            return xml_type[type]
        pass

    def close(self):
        if self.fw:
            self.fw.close()


def GenObj(G, name, shortObjectName, mulNodeFlag):
    G.bodyEnd()
    G.GenEnum(shortObjectName)

    if mulNodeFlag:
        G.headLink(name, shortObjectName + 'LINK')

    if mulNodeFlag:
        G.setfunc()
        G.getfunc()
        G.ObjGenFunc()
    else:
        G.setSingleFunc()
        G.getSingleFunc()
        pass

    # head prmt head file
    G.headFilePrmt(mulNodeFlag)
    # prmt file end

    # igd file begain
    G.GenStruct(mulNodeFlag)

    G.igdGenfile()

    if mulNodeFlag:
        G.igdAddfun(shortObjectName)
        G.igdDelfun(shortObjectName)
        G.igdGetfun(shortObjectName)
        G.igdSetfun(shortObjectName)
        G.igdGetNumfun(shortObjectName)
        G.igdGetAllNumfun(shortObjectName)
        G.igdGetAllInfofun(shortObjectName)
        G.igdMulInit(shortObjectName)
    else:
        G.igdSingleGetfun(shortObjectName)
        G.igdSingleSetfun(shortObjectName)
        G.igdinit(shortObjectName)

    G.close()


# 示例用法
if __name__ == "__main__":
    xml_file = r"E:\mypython_new\file_IO\cms-dm-hg-cmcc-tr98-obj-Traffic.xml"  # 替换为你的 XML 文件路径

    with open(xml_file, 'r') as fr:
        L = fr.readlines()
        # print(L)
        shortObjectName = ''
        mulNodeFlag = False

        # prmt file begain
        name = ''
        j = 0
        objDict = []
        G = GenerateObject()
        for line in L:
            # print(line)
            if 'object' in line:
                if j:
                    GenObj(G, name, shortObjectName, mulNodeFlag)
                    del G
                    G = GenerateObject()

                G.headfile = False

                shortObjectName = ''
                soup = BeautifulSoup(line.strip(), "lxml")
                soup.prettify()
                # print(soup)
                for jpg_url in soup.find_all('object'):
                    # print(jpg_url.attrs)
                    for key, val in jpg_url.attrs.items():
                        # print('parent 0', key, val)
                        if key == 'shortobjectname':
                            # print('parent 1', key, val)
                            shortObjectName = val
                        elif key == 'name':
                            name = val
                        elif key == 'oid':
                            oid = val

                    if shortObjectName and name:
                        names = name.split('.')
                        print('zzzzzzzzzz', names)
                        if names[-2] == '{i}':
                            objName = names[-3]
                            mulNodeFlag = True
                        else:
                            objName = names[-2]
                            mulNodeFlag = False

                        # i = 0
                        # for list in names:
                        #     print(list)
                        #     if not objDict[list]:
                        #         objDict[list] = []
                        #     else:
                        #         objDict[list]

                        # print("objDict", objDict)
                        #
                        # print(f"zzzzzzzzzzzz222 {objName}\n\n")
                        # shortObjectName = objName

                        if mulNodeFlag:
                            G.headObj(objName, name, oid)

                        G.head(name, objName)

            elif 'parameter' in line:
                soup = BeautifulSoup(line.strip(), "lxml")
                soup.prettify()
                # print(soup)
                for jpg_url in soup.find_all('parameter'):
                    # print(jpg_url.attrs)
                    name = ''
                    type = ''
                    flag = ''
                    maxlength = ''
                    maxValue = ''
                    dict = {}
                    for key, val in jpg_url.attrs.items():
                        # print(key, val)
                        dict[key] = val
                        if key == 'hideObjectFromAcs':
                            flag = flag + flags[val]
                        elif key == 'name':
                            name = val
                        elif key == 'type':
                            typehg = types[val]
                        elif key == 'supportlevel':
                            flag = flags[val]
                        elif key == 'maxlength':
                            maxlength = val
                        elif key == 'minValue':
                            minValue = val
                        elif key == 'maxValue':
                            maxValue = val

                    if name and typehg and flag:
                        G.body(shortObjectName, name, typehg, flag, dict)

            j = j + 1

        GenObj(G, name, shortObjectName, mulNodeFlag)
        print(objDict)
        G.headMulObj(objDict)

        del G
