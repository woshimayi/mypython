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


word32 igdCmIpSecVpnGet(uword8 *pucInfo, uword32 len)
{
	word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdIpSecVpnTab entry;
	IgdIpSecVpnTab *currObj = NULL;

	currObj = (IgdIpSecVpnTab *)pucInfo;
	HI_OS_MEMSET_S(&entry, sizeof(IgdIpSecVpnTab), 0, sizeof(IgdIpSecVpnTab));

	if (mib_chain_get(IGD_IPSECVPN_TAB, 0, (void *)&entry))
	{
		HI_OS_MEMCPY_S(currObj, sizeof(IgdIpSecVpnTab), &entry, sizeof(IgdIpSecVpnTab));
		lRet = IGD_CM_OPERATE_SUCCESS;
	}
	else
	{
		CM_LOG("mib_chain_get IGD_IPSECVPN_TAB is fail.\t\n");
		lRet = IGD_CM_OPERATE_FAIL;
	}

	return lRet;
}

word32 igdCmIpSecVpnSet(uword8 *pucInfo, uword32 len)
{
	CM_LOG("*************entry in igdCmSecureMacFilterAttrSet*************\n");

	IgdIpSecVpnTab currObj;
	IgdIpSecVpnTab *newObjTmp = NULL;

	if (!pucInfo)
		return (IGD_CM_GLOBAL_INPUT_PARA_ERROR);

	newObjTmp = (IgdIpSecVpnTab *)pucInfo;
	HI_OS_MEMSET_S(&currObj, sizeof(IgdIpSecVpnTab), 0, sizeof(IgdIpSecVpnTab));
	if (0 == mib_chain_get(IGD_IPSECVPN_TAB, 0, (void *)&currObj))
	{
		CM_LOG("mib_chain_get IGD_IPSECVPN_TAB is fail.\t\n");
		mib_chain_add(IGD_IPSECVPN_TAB, (void *)&currObj);
	}


                if ((newObjTmp->ulBitmap & IPSECVPN_ATTR_MASK_BIT0_MAXNUMBEROFENTRIES) == IPSECVPN_ATTR_MASK_BIT0_MAXNUMBEROFENTRIES)
                {
                    currObj.MaxNumberOfEntries = newObjTmp->MaxNumberOfEntries;
                }
                if ((newObjTmp->ulBitmap & IPSECVPN_ATTR_MASK_BIT1_IPSECVPNNUMBEROFENTRIES) == IPSECVPN_ATTR_MASK_BIT1_IPSECVPNNUMBEROFENTRIES)
                {
                    currObj.IPSecVPNNumberOfEntries = newObjTmp->IPSecVPNNumberOfEntries;
                }
	mib_chain_update(IGD_IPSECVPN_TAB, (void *)&currObj, 0);

	return 0;
}

word32 igdCmIpSecVpnInit(void)
{
	CM_LOG("############ Timed Task Attribute Table Init Start ############\n");

	word32 lInsNum = 0, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdIpSecVpnTab entry;
	IgdIpSecVpnTab IgdIpSecVpnTabTmp, *pIgdIpSecVpnTabTmp = NULL;

	pIgdIpSecVpnTabTmp = &IgdIpSecVpnTabTmp;
	HI_OS_MEMSET_S(&entry, sizeof(IgdIpSecVpnTab), 0, sizeof(IgdIpSecVpnTab));
	HI_OS_MEMSET_S(pIgdIpSecVpnTabTmp, sizeof(IgdIpSecVpnTab), 0, sizeof(IgdIpSecVpnTab));

	mib_chain_get(IGD_IPSECVPN_TAB, lInsNum, &entry);

	HI_OS_MEMCPY_S(pIgdIpSecVpnTabTmp, sizeof(*pIgdIpSecVpnTabTmp), &entry, sizeof(IgdIpSecVpnTab));

	lRet = igdCmIpSecVpnSet((uword8 *)pIgdIpSecVpnTabTmp, sizeof(IgdIpSecVpnTab));
	if (IGD_CM_OPERATE_SUCCESS != lRet)
	{
		CM_LOG("############ Timed Task Attribute Table Init Failed ############\n");
	}

	CM_LOG("############  Timed Task Attribute Table Init End ############\n");

	return lRet;
}

        