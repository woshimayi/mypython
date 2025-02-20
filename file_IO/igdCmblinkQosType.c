#include "mib.h"
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
#define CM_LOG(fmt, args...) hi_debug(HI_SUBMODULE_CM_QOS, "[CM:%s(%d)]" fmt "\r\n", __func__, __LINE__, ##args)
#define CM_ERR(fmt, args...) printf("[CM:%s(%d)]" fmt "\r\n", __func__, __LINE__, ##args)


word32 igdCmBlinkQosTypeAdd(uword8 *pucInfo, uword32 len)
{
    word32  totalNum = 0, lInsNum = 0, lIndex = 0;
	word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdBlinkQosTypeTab currObj;
	IgdBlinkQosTypeTab entry;
	IgdBlinkQosTypeTab  *newObj = (IgdBlinkQosTypeTab *)pucInfo;

	totalNum = mib_chain_total(IGD_BLINKQOSTYPE_TAB);
	CM_LOG("totalNum = %d", totalNum);

	for (lInsNum = 0; lInsNum < totalNum; lInsNum++)
	{
		HI_OS_MEMSET_S(&entry, sizeof(IgdBlinkQosTypeTab), 0, sizeof(IgdBlinkQosTypeTab));
		if (! mib_chain_get(IGD_BLINKQOSTYPE_TAB, lInsNum, (void *)&entry))
			continue;
		CM_LOG("ulIndex = %d", entry.ulIndex);

		if (entry.ulIndex > lIndex)
			lIndex = entry.ulIndex;
	}

	HI_OS_MEMSET_S(&currObj, sizeof(IgdBlinkQosTypeTab), 0, sizeof(IgdBlinkQosTypeTab));
	HI_OS_MEMCPY_S(&entry, sizeof(IgdBlinkQosTypeTab), newObj, sizeof(IgdBlinkQosTypeTab));
	entry.ulIndex = lInsNum + 1;
	entry.ulStateAndIndex = 0;
	CM_LOG("ulIndex = %d", entry.ulIndex);
	if (!totalNum)
	{
		currObj.ulIndex = 1;
	}
	CM_LOG("ulIndex = %d", entry.ulIndex);
	if (mib_chain_add(IGD_BLINKQOSTYPE_TAB, (unsigned char *)&entry))
	{
		/*backfill TaskId*/
		lRet = IGD_CM_OPERATE_SUCCESS;
	}
	newObj->ulIndex = lIndex + 1;
	return lRet;
}

word32 igdCmBlinkQosTypeDel(uword8 *pucInfo, uword32 len)
        {
	word32 i = 0, totalNum = 0;
	IgdBlinkQosTypeTab *pcurrObj = (IgdBlinkQosTypeTab *)pucInfo;
	IgdBlinkQosTypeTab currObj;

	CM_LOG("ulIndex = %d", pcurrObj->ulIndex);

	totalNum = mib_chain_total(IGD_BLINKQOSTYPE_TAB);
	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&currObj, sizeof(currObj), 0, sizeof(currObj));
		if (!mib_chain_get(IGD_BLINKQOSTYPE_TAB, i, (void *)&currObj))
		{
			continue;
		}
		if (pcurrObj->ulIndex == currObj.ulIndex)
		{
			break;
		}
	}
	CM_LOG("ulStateAndIndex=%d ulIndex = %d not found.\r\n", pcurrObj->ulStateAndIndex, pcurrObj->ulIndex);

	if (i >= totalNum)
	{
		CM_LOG("ulStateAndIndex=%d ulIndex = %d  not found.\r\n", pcurrObj->ulStateAndIndex, pcurrObj->ulStateAndIndex);
		return IGD_CM_OPERATE_FAIL;
	}

	mib_chain_delete(IGD_BLINKQOSTYPE_TAB, i);
	return IGD_CM_OPERATE_SUCCESS;
}

word32 igdCmBlinkQosTypeGet(uword8 *pucInfo, uword32 len)
{
	word32 i, totalNum, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdBlinkQosTypeTab currObj;
	IgdBlinkQosTypeTab *newObj = NULL;

	newObj = (IgdBlinkQosTypeTab *)pucInfo;

	CM_LOG("ulIndex=%d \r\n", newObj->ulIndex);

	totalNum = mib_chain_total(IGD_BLINKQOSTYPE_TAB);
	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&currObj, sizeof(currObj), 0, sizeof(currObj));
		if (!mib_chain_get(IGD_BLINKQOSTYPE_TAB, i, (void *)&currObj))
		{
			continue;
		}
		CM_LOG("i=%d ulIndex=%d currObj.ulIndex = %d newObj->ulIndex = %d\n",  i, currObj.ulIndex, currObj.ulIndex,
		       newObj->ulIndex);

		if (currObj.ulIndex == newObj->ulIndex)
		{
			break;
		}
	}
	if (i >= totalNum)
	{
		CM_LOG("taskId=%d not found.\r\n", newObj->ulIndex);
		return IGD_CM_OPERATE_FAIL;
	}

	/*backfill value*/
	HI_OS_MEMCPY_S(newObj, sizeof(*newObj), &currObj, sizeof(IgdBlinkQosTypeTab));

	return lRet;
}

word32 igdCmBlinkQosTypeSet(uword8 *pucInfo, uword32 len)
{	
    word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdBlinkQosTypeTab currObj;
	IgdBlinkQosTypeTab IgdBlinkQosTypeTabTmp, *newObjTmp = NULL;
	word32 i, totalNum;

	newObjTmp = &IgdBlinkQosTypeTabTmp;
	HI_OS_MEMSET_S(newObjTmp, sizeof(IgdBlinkQosTypeTab), 0, sizeof(IgdBlinkQosTypeTab));
	HI_OS_MEMCPY_S(newObjTmp, sizeof(*newObjTmp), pucInfo, sizeof(IgdBlinkQosTypeTab));
	HI_OS_MEMSET_S(&currObj, sizeof(IgdBlinkQosTypeTab), 0, sizeof(IgdBlinkQosTypeTab));

	totalNum = mib_chain_total(IGD_BLINKQOSTYPE_TAB);
	CM_LOG("totalNum = %d", totalNum);
	for (i = 0; i < totalNum; i++)
	{
		if (!mib_chain_get(IGD_BLINKQOSTYPE_TAB, i, (void *)&currObj))
		{
			continue;
		}
		CM_LOG("i=%d ulIndex=%d\n", i, currObj.ulIndex);

		if (currObj.ulIndex == newObjTmp->ulIndex)
		{
			break;
		}
	}
	if (i == totalNum)
	{
		CM_LOG("task id %d not found.\r\n", newObjTmp->ulIndex);
		return IGD_CM_OPERATE_FAIL;
	}

// un todo



	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT0_QOSPRIORITY) == BLINKQOSTYPE_ATTR_MASK_BIT0_QOSPRIORITY)
	{
	    currObj.QosPriority = newObjTmp->QosPriority;
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT1_DSCPENABLE) == BLINKQOSTYPE_ATTR_MASK_BIT1_DSCPENABLE)
	{
	    currObj.DscpEnable = newObjTmp->DscpEnable;
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT2_DSCPPRIORITY) == BLINKQOSTYPE_ATTR_MASK_BIT2_DSCPPRIORITY)
	{
	    currObj.DscpPriority = newObjTmp->DscpPriority;
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT3_VLAN8021PENABLE) == BLINKQOSTYPE_ATTR_MASK_BIT3_VLAN8021PENABLE)
	{
	    currObj.Vlan8021pEnable = newObjTmp->Vlan8021pEnable;
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT4_VLAN8021P) == BLINKQOSTYPE_ATTR_MASK_BIT4_VLAN8021P)
	{
	    currObj.Vlan8021p = newObjTmp->Vlan8021p;
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT5_SOURCEIP) == BLINKQOSTYPE_ATTR_MASK_BIT5_SOURCEIP)
	{
	    HI_OS_MEMCPY_S(currObj.SourceIp, sizeof(currObj.SourceIp), newObjTmp->SourceIp, sizeof(currObj.SourceIp));
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT6_SOURCEPORT) == BLINKQOSTYPE_ATTR_MASK_BIT6_SOURCEPORT)
	{
	    currObj.SourcePort = newObjTmp->SourcePort;
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT7_DESTINATIONIP) == BLINKQOSTYPE_ATTR_MASK_BIT7_DESTINATIONIP)
	{
	    HI_OS_MEMCPY_S(currObj.DestinationIp, sizeof(currObj.DestinationIp), newObjTmp->DestinationIp, sizeof(currObj.DestinationIp));
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT8_DESTINATIONPORT) == BLINKQOSTYPE_ATTR_MASK_BIT8_DESTINATIONPORT)
	{
	    currObj.DestinationPort = newObjTmp->DestinationPort;
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT9_PROTOCOL) == BLINKQOSTYPE_ATTR_MASK_BIT9_PROTOCOL)
	{
	    HI_OS_MEMCPY_S(currObj.Protocol, sizeof(currObj.Protocol), newObjTmp->Protocol, sizeof(currObj.Protocol));
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT10_SOURCEMAC) == BLINKQOSTYPE_ATTR_MASK_BIT10_SOURCEMAC)
	{
	    HI_OS_MEMCPY_S(currObj.SourceMac, sizeof(currObj.SourceMac), newObjTmp->SourceMac, sizeof(currObj.SourceMac));
	}
	if ((newObjTmp->ulBitmap & BLINKQOSTYPE_ATTR_MASK_BIT11_DESTINATIONMAC) == BLINKQOSTYPE_ATTR_MASK_BIT11_DESTINATIONMAC)
	{
	    HI_OS_MEMCPY_S(currObj.DestinationMac, sizeof(currObj.DestinationMac), newObjTmp->DestinationMac, sizeof(currObj.DestinationMac));
	}
	lRet = mib_chain_update(IGD_BLINKQOSTYPE_TAB, (void *)&currObj, i);
	if (!lRet)
	{
		CM_LOG("lRet(%d): mib_chain_update(IGD_BLINKQOSTYPE_TAB, (void *)&currObj, 0) failed !!!", lRet);
		return lRet;
	}
	CM_LOG("lRet = %d", lRet);

	return 0;
}

word32 igdCmBlinkQosTypeGetNum(uword32 *entrynum)
{
	*entrynum = mib_chain_total(IGD_BLINKQOSTYPE_TAB);
	CM_LOG("entrynum [%d].\r\n", *entrynum);
	return IGD_CM_OPERATE_SUCCESS;
}

word32 igdCmBlinkQosTypeGetAllIndex(uword8 *pucInfo, uword32 len)
{
	uword32 allIndex[IGD_TIMED_TASK_NUM];
	word32 i, j = 0, totalTaskNum;
	IgdBlinkQosTypeTab qosEntry;

	totalTaskNum = mib_chain_total(IGD_BLINKQOSTYPE_TAB);
	CM_LOG("totalTaskNum  = %d", totalTaskNum);
	for (i = 0; i < totalTaskNum; i++)
	{
		HI_OS_MEMSET_S(&qosEntry, sizeof(qosEntry), 0, sizeof(qosEntry));
		if (!mib_chain_get(IGD_BLINKQOSTYPE_TAB, i, (void *)&qosEntry))
		{
			continue;
		}
		allIndex[j] = qosEntry.ulIndex;
		CM_LOG("allIndex[%d] = [%d].\r\n", j, allIndex[j]);
		j++;
	}

	HI_OS_MEMCPY_S(pucInfo, (sizeof(uword32)*totalTaskNum), allIndex, (sizeof(uword32)*totalTaskNum));

	return IGD_CM_OPERATE_SUCCESS;
}

word32 igdCmBlinkQosTypeGetAllInfo(uword8 *pucInfo, uword32 len)
{
	word32 i, j = 0, totalNum, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdBlinkQosTypeTab tmpObj;
	IgdBlinkQosTypeTab *newObj = NULL;

	newObj = (IgdBlinkQosTypeTab *)pucInfo;

	totalNum = mib_chain_total(IGD_BLINKQOSTYPE_TAB);
	CM_LOG("totalNum  = %d", totalNum);
	if (0 == totalNum)
	{
		CM_LOG("aosnet timed task is empty !\r\n");
		return IGD_CM_OPERATE_FAIL;
	}

	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&tmpObj, sizeof(tmpObj), 0, sizeof(tmpObj));
		if (!mib_chain_get(IGD_BLINKQOSTYPE_TAB, i, (void *)&tmpObj))
		{
			continue;
		}
		CM_LOG("ulStateAndIndex = %d ulIndex = %d", tmpObj.ulStateAndIndex, tmpObj.ulIndex);
		HI_OS_MEMCPY_S(&newObj[j], sizeof(IgdBlinkQosTypeTab), &tmpObj, sizeof(IgdBlinkQosTypeTab));
		j++;
	}

	return lRet;
}

word32 igdCmBlinkQosTypeInit(void)
{
	CM_LOG("############ Timed Task Attribute Table Init Start ############\n");
	word32 lRet = IGD_CM_OPERATE_SUCCESS;

	unsigned int MaxInstNum = 0;
	unsigned int msgLen = 0;
	IgdBlinkQosTypeTab *pstParaList = NULL;
	IgdBlinkQosTypeTab  entry;

	MaxInstNum = mib_chain_total(IGD_BLINKQOSTYPE_TAB);
	if (MaxInstNum == 0) {
		CM_LOG("MAC Filte list table is empty !\r\n");
		return IGD_CM_OPERATE_SUCCESS;
	}

	CM_LOG("INIT IGD.X_CMCC_Security.MacFilter.obj	NUM=[%d]\n", MaxInstNum);
	if (MaxInstNum == 0)
		return 0;
	
	pstParaList = (IgdBlinkQosTypeTab *)malloc(MaxInstNum * sizeof(IgdBlinkQosTypeTab));
	if (NULL == pstParaList)
		return 0;
	HI_OS_MEMSET_S((char *)pstParaList, MaxInstNum * sizeof(IgdBlinkQosTypeTab), 0, MaxInstNum * sizeof(IgdBlinkQosTypeTab));
	msgLen = MaxInstNum * sizeof(IgdBlinkQosTypeTab);

	lRet = igdCmConfGetAllEntry(IGD_BLINKQOSTYPE_TAB,(void *)(pstParaList), msgLen);
	if(lRet != IGD_CM_OPERATE_SUCCESS )
	{
		CM_LOG("[CWMP] GETALL IGD_BLINKQOSTYPE_TAB FAIL.(ret:%x)", lRet);
		return -1;
	}
	
	for (int ulloop = 0; ulloop < MaxInstNum; ulloop++)
	{
		if (! mib_chain_get(IGD_BLINKQOSTYPE_TAB, ulloop, (void *)&entry))
			continue;

		CM_LOG("INIT INIT InternetGatewayDevice.AhsapiQos.DscpPriority INDEX=[%d]\n", pstParaList[ulloop].ulIndex);
		lRet = igdCmBlinkQosTypeSet((uword8 *)&entry, sizeof(IgdBlinkQosTypeTab));
		if (IGD_CM_OPERATE_SUCCESS != lRet)
		{
			CM_LOG("############ Timed Task Attribute Table Init Failed ############\n");
		}
	}
	free(pstParaList);

	return lRet;
}

