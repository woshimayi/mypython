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


word32 igdCmIPsecConfigAdd(uword8 *pucInfo, uword32 len)
{
    word32  totalNum = 0, lInsNum = 0, lIndex = 0;
	word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdIPsecConfigTab currObj;
	IgdIPsecConfigTab entry;
	IgdIPsecConfigTab  *newObj = (IgdIPsecConfigTab *)pucInfo;

	totalNum = mib_chain_total(IGD_IPSECCONFIG_TAB);
	CM_LOG("totalNum = %d", totalNum);

	for (lInsNum = 0; lInsNum < totalNum; lInsNum++)
	{
		HI_OS_MEMSET_S(&entry, sizeof(IgdIPsecConfigTab), 0, sizeof(IgdIPsecConfigTab));
		if (! mib_chain_get(IGD_IPSECCONFIG_TAB, lInsNum, (void *)&entry))
			continue;
		CM_LOG("ulIndex = %d", entry.ulIndex);

		if (entry.ulIndex > lIndex)
			lIndex = entry.ulIndex;
	}

	HI_OS_MEMSET_S(&currObj, sizeof(IgdIPsecConfigTab), 0, sizeof(IgdIPsecConfigTab));
	HI_OS_MEMCPY_S(&entry, sizeof(IgdIPsecConfigTab), newObj, sizeof(IgdIPsecConfigTab));
	entry.ulIndex = lIndex + 1;
	entry.ulStateAndIndex = 0;
	CM_LOG("ulIndex = %d", entry.ulIndex);
	if (!totalNum)
	{
		currObj.ulIndex = 1;
	}
	CM_LOG("ulIndex = %d", entry.ulIndex);
	if (mib_chain_add(IGD_IPSECCONFIG_TAB, (unsigned char *)&entry))
	{
		/*backfill TaskId*/
		lRet = IGD_CM_OPERATE_SUCCESS;
	}
	newObj->ulIndex = lIndex + 1;
	return lRet;
}

word32 igdCmIPsecConfigDel(uword8 *pucInfo, uword32 len)
        {
	word32 i = 0, totalNum = 0;
	IgdIPsecConfigTab *pcurrObj = (IgdIPsecConfigTab *)pucInfo;
	IgdIPsecConfigTab currObj;

	CM_LOG("ulIndex = %d", pcurrObj->ulIndex);

	totalNum = mib_chain_total(IGD_IPSECCONFIG_TAB);
	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&currObj, sizeof(currObj), 0, sizeof(currObj));
		if (!mib_chain_get(IGD_IPSECCONFIG_TAB, i, (void *)&currObj))
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

	mib_chain_delete(IGD_IPSECCONFIG_TAB, i);
	return IGD_CM_OPERATE_SUCCESS;
}

word32 igdCmIPsecConfigGet(uword8 *pucInfo, uword32 len)
{
	word32 i, totalNum, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdIPsecConfigTab currObj;
	IgdIPsecConfigTab *newObj = NULL;

	newObj = (IgdIPsecConfigTab *)pucInfo;

	CM_LOG("ulIndex=%d \r\n", newObj->ulIndex);

	totalNum = mib_chain_total(IGD_IPSECCONFIG_TAB);
	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&currObj, sizeof(currObj), 0, sizeof(currObj));
		if (!mib_chain_get(IGD_IPSECCONFIG_TAB, i, (void *)&currObj))
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
	HI_OS_MEMCPY_S(newObj, sizeof(*newObj), &currObj, sizeof(IgdIPsecConfigTab));

	return lRet;
}

word32 igdCmIPsecConfigSet(uword8 *pucInfo, uword32 len)
{	
    word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdIPsecConfigTab currObj;
	IgdIPsecConfigTab IgdIPsecConfigTabTmp, *newObjTmp = NULL;
	word32 i, totalNum;

	newObjTmp = &IgdIPsecConfigTabTmp;
	HI_OS_MEMSET_S(newObjTmp, sizeof(IgdIPsecConfigTab), 0, sizeof(IgdIPsecConfigTab));
	HI_OS_MEMCPY_S(newObjTmp, sizeof(*newObjTmp), pucInfo, sizeof(IgdIPsecConfigTab));
	HI_OS_MEMSET_S(&currObj, sizeof(IgdIPsecConfigTab), 0, sizeof(IgdIPsecConfigTab));

	totalNum = mib_chain_total(IGD_IPSECCONFIG_TAB);
	CM_LOG("totalNum = %d", totalNum);
	for (i = 0; i < totalNum; i++)
	{
		if (!mib_chain_get(IGD_IPSECCONFIG_TAB, i, (void *)&currObj))
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



                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT0_NAME) == IPSECCONFIG_ATTR_MASK_BIT0_NAME)
                {
                    HI_OS_MEMCPY_S(currObj.Name, sizeof(currObj.Name), newObjTmp->Name, sizeof(currObj.Name));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT1_ENABLE) == IPSECCONFIG_ATTR_MASK_BIT1_ENABLE)
                {
                    currObj.Enable = newObjTmp->Enable;
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT2_IPSECTYPE) == IPSECCONFIG_ATTR_MASK_BIT2_IPSECTYPE)
                {
                    HI_OS_MEMCPY_S(currObj.IPSecType, sizeof(currObj.IPSecType), newObjTmp->IPSecType, sizeof(currObj.IPSecType));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT3_REMOTESUBNET) == IPSECCONFIG_ATTR_MASK_BIT3_REMOTESUBNET)
                {
                    HI_OS_MEMCPY_S(currObj.RemoteSubnet, sizeof(currObj.RemoteSubnet), newObjTmp->RemoteSubnet, sizeof(currObj.RemoteSubnet));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT4_LOCALSUBNET) == IPSECCONFIG_ATTR_MASK_BIT4_LOCALSUBNET)
                {
                    HI_OS_MEMCPY_S(currObj.LocalSubnet, sizeof(currObj.LocalSubnet), newObjTmp->LocalSubnet, sizeof(currObj.LocalSubnet));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT5_REMOTEIP) == IPSECCONFIG_ATTR_MASK_BIT5_REMOTEIP)
                {
                    HI_OS_MEMCPY_S(currObj.RemoteIP, sizeof(currObj.RemoteIP), newObjTmp->RemoteIP, sizeof(currObj.RemoteIP));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT6_REMOTEDOMAIN) == IPSECCONFIG_ATTR_MASK_BIT6_REMOTEDOMAIN)
                {
                    HI_OS_MEMCPY_S(currObj.RemoteDomain, sizeof(currObj.RemoteDomain), newObjTmp->RemoteDomain, sizeof(currObj.RemoteDomain));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT7_EXCHANGEMODE) == IPSECCONFIG_ATTR_MASK_BIT7_EXCHANGEMODE)
                {
                    HI_OS_MEMCPY_S(currObj.ExchangeMode, sizeof(currObj.ExchangeMode), newObjTmp->ExchangeMode, sizeof(currObj.ExchangeMode));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT8_IKEAUTHENTICATIONALGORITHM) == IPSECCONFIG_ATTR_MASK_BIT8_IKEAUTHENTICATIONALGORITHM)
                {
                    HI_OS_MEMCPY_S(currObj.IKEAuthenticationAlgorithm, sizeof(currObj.IKEAuthenticationAlgorithm), newObjTmp->IKEAuthenticationAlgorithm, sizeof(currObj.IKEAuthenticationAlgorithm));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT9_IKEAUTHENTICATIONMETHOD) == IPSECCONFIG_ATTR_MASK_BIT9_IKEAUTHENTICATIONMETHOD)
                {
                    HI_OS_MEMCPY_S(currObj.IKEAuthenticationMethod, sizeof(currObj.IKEAuthenticationMethod), newObjTmp->IKEAuthenticationMethod, sizeof(currObj.IKEAuthenticationMethod));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT10_IKEENCRYPTIONALGORITHM) == IPSECCONFIG_ATTR_MASK_BIT10_IKEENCRYPTIONALGORITHM)
                {
                    HI_OS_MEMCPY_S(currObj.IKEEncryptionAlgorithm, sizeof(currObj.IKEEncryptionAlgorithm), newObjTmp->IKEEncryptionAlgorithm, sizeof(currObj.IKEEncryptionAlgorithm));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT11_IKEDHGROUP) == IPSECCONFIG_ATTR_MASK_BIT11_IKEDHGROUP)
                {
                    HI_OS_MEMCPY_S(currObj.IKEDHGroup, sizeof(currObj.IKEDHGroup), newObjTmp->IKEDHGroup, sizeof(currObj.IKEDHGroup));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT12_IKEIDTYPE) == IPSECCONFIG_ATTR_MASK_BIT12_IKEIDTYPE)
                {
                    HI_OS_MEMCPY_S(currObj.IKEIDType, sizeof(currObj.IKEIDType), newObjTmp->IKEIDType, sizeof(currObj.IKEIDType));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT13_IKELOCALNAME) == IPSECCONFIG_ATTR_MASK_BIT13_IKELOCALNAME)
                {
                    HI_OS_MEMCPY_S(currObj.IKELocalName, sizeof(currObj.IKELocalName), newObjTmp->IKELocalName, sizeof(currObj.IKELocalName));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT14_IKEREMOTENAME) == IPSECCONFIG_ATTR_MASK_BIT14_IKEREMOTENAME)
                {
                    HI_OS_MEMCPY_S(currObj.IKERemoteName, sizeof(currObj.IKERemoteName), newObjTmp->IKERemoteName, sizeof(currObj.IKERemoteName));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT15_IKEPRESHAREKEY) == IPSECCONFIG_ATTR_MASK_BIT15_IKEPRESHAREKEY)
                {
                    HI_OS_MEMCPY_S(currObj.IKEPreshareKey, sizeof(currObj.IKEPreshareKey), newObjTmp->IKEPreshareKey, sizeof(currObj.IKEPreshareKey));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT16_IPSECOUTINTERFACE) == IPSECCONFIG_ATTR_MASK_BIT16_IPSECOUTINTERFACE)
                {
                    HI_OS_MEMCPY_S(currObj.IPSecOutInterface, sizeof(currObj.IPSecOutInterface), newObjTmp->IPSecOutInterface, sizeof(currObj.IPSecOutInterface));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT17_IPSECENCAPSULATIONMODE) == IPSECCONFIG_ATTR_MASK_BIT17_IPSECENCAPSULATIONMODE)
                {
                    HI_OS_MEMCPY_S(currObj.IPSecEncapsulationMode, sizeof(currObj.IPSecEncapsulationMode), newObjTmp->IPSecEncapsulationMode, sizeof(currObj.IPSecEncapsulationMode));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT18_IPSECTRANSFORM) == IPSECCONFIG_ATTR_MASK_BIT18_IPSECTRANSFORM)
                {
                    HI_OS_MEMCPY_S(currObj.IPSecTransform, sizeof(currObj.IPSecTransform), newObjTmp->IPSecTransform, sizeof(currObj.IPSecTransform));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT19_ESPAUTHENTICATIONALGORITHM) == IPSECCONFIG_ATTR_MASK_BIT19_ESPAUTHENTICATIONALGORITHM)
                {
                    HI_OS_MEMCPY_S(currObj.ESPAuthenticationAlgorithm, sizeof(currObj.ESPAuthenticationAlgorithm), newObjTmp->ESPAuthenticationAlgorithm, sizeof(currObj.ESPAuthenticationAlgorithm));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT20_ESPENCRYPTIONALGORITHM) == IPSECCONFIG_ATTR_MASK_BIT20_ESPENCRYPTIONALGORITHM)
                {
                    HI_OS_MEMCPY_S(currObj.ESPEncryptionAlgorithm, sizeof(currObj.ESPEncryptionAlgorithm), newObjTmp->ESPEncryptionAlgorithm, sizeof(currObj.ESPEncryptionAlgorithm));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT21_IPSECPFS) == IPSECCONFIG_ATTR_MASK_BIT21_IPSECPFS)
                {
                    HI_OS_MEMCPY_S(currObj.IPSecPFS, sizeof(currObj.IPSecPFS), newObjTmp->IPSecPFS, sizeof(currObj.IPSecPFS));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT22_IKESAPERIOD) == IPSECCONFIG_ATTR_MASK_BIT22_IKESAPERIOD)
                {
                    currObj.IKESAPeriod = newObjTmp->IKESAPeriod;
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT23_IPSECSATIMEPERIOD) == IPSECCONFIG_ATTR_MASK_BIT23_IPSECSATIMEPERIOD)
                {
                    currObj.IPSecSATimePeriod = newObjTmp->IPSecSATimePeriod;
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT24_IPSECSATRAFFICPERIOD) == IPSECCONFIG_ATTR_MASK_BIT24_IPSECSATRAFFICPERIOD)
                {
                    currObj.IPSecSATrafficPeriod = newObjTmp->IPSecSATrafficPeriod;
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT25_AHAUTHENTICATIONALGORITHM) == IPSECCONFIG_ATTR_MASK_BIT25_AHAUTHENTICATIONALGORITHM)
                {
                    HI_OS_MEMCPY_S(currObj.AHAuthenticationAlgorithm, sizeof(currObj.AHAuthenticationAlgorithm), newObjTmp->AHAuthenticationAlgorithm, sizeof(currObj.AHAuthenticationAlgorithm));
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT26_DPDENABLE) == IPSECCONFIG_ATTR_MASK_BIT26_DPDENABLE)
                {
                    currObj.DPDEnable = newObjTmp->DPDEnable;
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT27_DPDTHRESHOLD) == IPSECCONFIG_ATTR_MASK_BIT27_DPDTHRESHOLD)
                {
                    currObj.DPDThreshold = newObjTmp->DPDThreshold;
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT28_DPDRETRY) == IPSECCONFIG_ATTR_MASK_BIT28_DPDRETRY)
                {
                    currObj.DPDRetry = newObjTmp->DPDRetry;
                }
                if ((newObjTmp->ulBitmap & IPSECCONFIG_ATTR_MASK_BIT29_CONNECTIONSTATUS) == IPSECCONFIG_ATTR_MASK_BIT29_CONNECTIONSTATUS)
                {
                    HI_OS_MEMCPY_S(currObj.ConnectionStatus, sizeof(currObj.ConnectionStatus), newObjTmp->ConnectionStatus, sizeof(currObj.ConnectionStatus));
                }
	lRet = mib_chain_update(IGD_IPSECCONFIG_TAB, (void *)&currObj, i);
	if (!lRet)
	{
		CM_LOG("lRet(%d): mib_chain_update(IGD_IPSECCONFIG_TAB, (void *)&currObj, 0) failed !!!", lRet);
		return lRet;
	}
	CM_LOG("lRet = %d", lRet);

	return 0;
}

word32 igdCmIPsecConfigGetNum(uword32 *entrynum)
{
	*entrynum = mib_chain_total(IGD_IPSECCONFIG_TAB);
	CM_LOG("entrynum [%d].\r\n", *entrynum);
	return IGD_CM_OPERATE_SUCCESS;
}

word32 igdCmIPsecConfigGetAllIndex(uword8 *pucInfo, uword32 len)
{
	uword32 allIndex[IGD_TIMED_TASK_NUM];
	word32 i, j = 0, totalTaskNum;
	IgdIPsecConfigTab qosEntry;

	totalTaskNum = mib_chain_total(IGD_IPSECCONFIG_TAB);
	CM_LOG("totalTaskNum  = %d", totalTaskNum);
	for (i = 0; i < totalTaskNum; i++)
	{
		HI_OS_MEMSET_S(&qosEntry, sizeof(qosEntry), 0, sizeof(qosEntry));
		if (!mib_chain_get(IGD_IPSECCONFIG_TAB, i, (void *)&qosEntry))
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

word32 igdCmIPsecConfigGetAllInfo(uword8 *pucInfo, uword32 len)
{
	word32 i, j = 0, totalNum, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdIPsecConfigTab tmpObj;
	IgdIPsecConfigTab *newObj = NULL;

	newObj = (IgdIPsecConfigTab *)pucInfo;

	totalNum = mib_chain_total(IGD_IPSECCONFIG_TAB);
	CM_LOG("totalNum  = %d", totalNum);
	if (0 == totalNum)
	{
		CM_LOG("aosnet timed task is empty !\r\n");
		return IGD_CM_OPERATE_FAIL;
	}

	for (i = 0; i < totalNum; i++)
	{
		HI_OS_MEMSET_S(&tmpObj, sizeof(tmpObj), 0, sizeof(tmpObj));
		if (!mib_chain_get(IGD_IPSECCONFIG_TAB, i, (void *)&tmpObj))
		{
			continue;
		}
		CM_LOG("ulStateAndIndex = %d ulIndex = %d", tmpObj.ulStateAndIndex, tmpObj.ulIndex);
		HI_OS_MEMCPY_S(&newObj[j], sizeof(IgdIPsecConfigTab), &tmpObj, sizeof(IgdIPsecConfigTab));
		j++;
	}

	return lRet;
}

word32 igdCmIPsecConfigInit(void)
{
	CM_LOG("############ Timed Task Attribute Table Init Start ############\n");
	word32 lRet = IGD_CM_OPERATE_SUCCESS;

	unsigned int MaxInstNum = 0;
	unsigned int msgLen = 0;
	IgdIPsecConfigTab *pstParaList = NULL;
	IgdIPsecConfigTab  entry;

	MaxInstNum = mib_chain_total(IGD_IPSECCONFIG_TAB);
	if (MaxInstNum == 0) {
		CM_LOG("MAC Filte list table is empty !\r\n");
		return IGD_CM_OPERATE_SUCCESS;
	}

	CM_LOG("INIT IGD.X_CMCC_Security.MacFilter.obj	NUM=[%d]\n", MaxInstNum);
	if (MaxInstNum == 0)
		return 0;
	
	pstParaList = (IgdIPsecConfigTab *)malloc(MaxInstNum * sizeof(IgdIPsecConfigTab));
	if (NULL == pstParaList)
		return 0;
	HI_OS_MEMSET_S((char *)pstParaList, MaxInstNum * sizeof(IgdIPsecConfigTab), 0, MaxInstNum * sizeof(IgdIPsecConfigTab));
	msgLen = MaxInstNum * sizeof(IgdIPsecConfigTab);

	lRet = igdCmConfGetAllEntry(IGD_IPSECCONFIG_TAB,(void *)(pstParaList), msgLen);
	if(lRet != IGD_CM_OPERATE_SUCCESS )
	{
		CM_LOG("[CWMP] GETALL IGD_IPSECCONFIG_TAB FAIL.(ret:%x)", lRet);
		return -1;
	}
	
	for (int ulloop = 0; ulloop < MaxInstNum; ulloop++)
	{
		if (! mib_chain_get(IGD_IPSECCONFIG_TAB, ulloop, (void *)&entry))
			continue;

		CM_LOG("INIT INIT InternetGatewayDevice.AhsapiQos.DscpPriority INDEX=[%d]\n", pstParaList[ulloop].ulIndex);
		lRet = igdCmIPsecConfigSet((uword8 *)&entry, sizeof(IgdIPsecConfigTab));
		if (IGD_CM_OPERATE_SUCCESS != lRet)
		{
			CM_LOG("############ Timed Task Attribute Table Init Failed ############\n");
		}
	}
	free(pstParaList);

	return lRet;
}

