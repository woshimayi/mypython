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


word32 igdCmBlinkQosGet(uword8 *pucInfo, uword32 len)
{
	word32 lRet;
	IgdBlinkQosTab entry;
	IgdBlinkQosTab *currObj = NULL;

	currObj = (IgdBlinkQosTab *)pucInfo;
	HI_OS_MEMSET_S(&entry, sizeof(IgdBlinkQosTab), 0, sizeof(IgdBlinkQosTab));

	if (mib_chain_get(IGD_BLINKQOS_TAB, 0, (void *)&entry))
	{
		HI_OS_MEMCPY_S(currObj, sizeof(IgdBlinkQosTab), &entry, sizeof(IgdBlinkQosTab));
		lRet = IGD_CM_OPERATE_SUCCESS;
	}
	else
	{
		CM_LOG("mib_chain_get IGD_BLINKQOS_TAB is fail.\t\n");
		lRet = IGD_CM_OPERATE_FAIL;
	}

	return lRet;
}

word32 igdCmBlinkQosSet(uword8 *pucInfo, uword32 len)
{
	CM_LOG("*************entry in igdCmSecureMacFilterAttrSet*************\n");

	IgdBlinkQosTab currObj;
	IgdBlinkQosTab *newObjTmp = NULL;

	if (!pucInfo)
		return (IGD_CM_GLOBAL_INPUT_PARA_ERROR);

	newObjTmp = (IgdBlinkQosTab *)pucInfo;
	HI_OS_MEMSET_S(&currObj, sizeof(IgdBlinkQosTab), 0, sizeof(IgdBlinkQosTab));
	if (0 == mib_chain_get(IGD_BLINKQOS_TAB, 0, (void *)&currObj))
	{
		CM_LOG("mib_chain_get IGD_BLINKQOS_TAB is fail.\t\n");
		mib_chain_add(IGD_BLINKQOS_TAB, (void *)&currObj);
	}


	if ((newObjTmp->ulBitmap & BLINKQOS_ATTR_MASK_BIT0_QOSENABLE) == BLINKQOS_ATTR_MASK_BIT0_QOSENABLE)
	{
	    currObj.QosEnable = newObjTmp->QosEnable;
	}
	if ((newObjTmp->ulBitmap & BLINKQOS_ATTR_MASK_BIT1_QOSPARAMETER) == BLINKQOS_ATTR_MASK_BIT1_QOSPARAMETER)
	{
	    HI_OS_MEMCPY_S(currObj.QosParameter, sizeof(currObj.QosParameter), newObjTmp->QosParameter, sizeof(currObj.QosParameter));
	}
	mib_chain_update(IGD_BLINKQOS_TAB, (void *)&currObj, 0);

	return 0;
}

word32 igdCmBlinkQosInit(void)
{
	CM_LOG("############ Timed Task Attribute Table Init Start ############\n");

	word32 lInsNum = 0, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdBlinkQosTab entry;
	IgdBlinkQosTab IgdBlinkQosTabTmp, *pIgdBlinkQosTabTmp = NULL;

	pIgdBlinkQosTabTmp = &IgdBlinkQosTabTmp;
	HI_OS_MEMSET_S(&entry, sizeof(IgdBlinkQosTab), 0, sizeof(IgdBlinkQosTab));
	HI_OS_MEMSET_S(pIgdBlinkQosTabTmp, sizeof(IgdBlinkQosTab), 0, sizeof(IgdBlinkQosTab));

	mib_chain_get(IGD_BLINKQOS_TAB, lInsNum, &entry);

	HI_OS_MEMCPY_S(pIgdBlinkQosTabTmp, sizeof(*pIgdBlinkQosTabTmp), &entry, sizeof(IgdBlinkQosTab));

	lRet = igdCmBlinkQosSet((uword8 *)pIgdBlinkQosTabTmp, sizeof(IgdBlinkQosTab));
	if (IGD_CM_OPERATE_SUCCESS != lRet)
	{
		CM_LOG("############ Timed Task Attribute Table Init Failed ############\n");
	}

	CM_LOG("############  Timed Task Attribute Table Init End ############\n");

	return lRet;
}

        