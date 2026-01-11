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


word32 igdCmBucpeGet(uword8 *pucInfo, uword32 len)
{
	word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdBucpeTab entry;
	IgdBucpeTab *currObj = NULL;

	currObj = (IgdBucpeTab *)pucInfo;
	HI_OS_MEMSET_S(&entry, sizeof(IgdBucpeTab), 0, sizeof(IgdBucpeTab));

	if (mib_chain_get(IGD_BUCPE_TAB, 0, (void *)&entry))
	{
		HI_OS_MEMCPY_S(currObj, sizeof(IgdBucpeTab), &entry, sizeof(IgdBucpeTab));
		lRet = IGD_CM_OPERATE_SUCCESS;
	}
	else
	{
		CM_LOG("mib_chain_get IGD_BUCPE_TAB is fail.\t\n");
		lRet = IGD_CM_OPERATE_FAIL;
	}

	return lRet;
}

word32 igdCmBucpeSet(uword8 *pucInfo, uword32 len)
{
	CM_LOG("*************entry in igdCmSecureMacFilterAttrSet*************\n");

	IgdBucpeTab currObj;
	IgdBucpeTab *newObjTmp = NULL;

	if (!pucInfo)
		return (IGD_CM_GLOBAL_INPUT_PARA_ERROR);

	newObjTmp = (IgdBucpeTab *)pucInfo;
	HI_OS_MEMSET_S(&currObj, sizeof(IgdBucpeTab), 0, sizeof(IgdBucpeTab));
	if (0 == mib_chain_get(IGD_BUCPE_TAB, 0, (void *)&currObj))
	{
		CM_LOG("mib_chain_get IGD_BUCPE_TAB is fail.\t\n");
		mib_chain_add(IGD_BUCPE_TAB, (void *)&currObj);
	}


                if ((newObjTmp->ulBitmap & BUCPE_ATTR_MASK_BIT0_ENABLE) == BUCPE_ATTR_MASK_BIT0_ENABLE)
                {
                    currObj.Enable = newObjTmp->Enable;
                }
	mib_chain_update(IGD_BUCPE_TAB, (void *)&currObj, 0);

	return 0;
}

word32 igdCmBucpeInit(void)
{
	CM_LOG("############ Timed Task Attribute Table Init Start ############\n");

	word32 lInsNum = 0, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdBucpeTab entry;
	IgdBucpeTab IgdBucpeTabTmp, *pIgdBucpeTabTmp = NULL;

	pIgdBucpeTabTmp = &IgdBucpeTabTmp;
	HI_OS_MEMSET_S(&entry, sizeof(IgdBucpeTab), 0, sizeof(IgdBucpeTab));
	HI_OS_MEMSET_S(pIgdBucpeTabTmp, sizeof(IgdBucpeTab), 0, sizeof(IgdBucpeTab));

	mib_chain_get(IGD_BUCPE_TAB, lInsNum, &entry);

	HI_OS_MEMCPY_S(pIgdBucpeTabTmp, sizeof(*pIgdBucpeTabTmp), &entry, sizeof(IgdBucpeTab));

	lRet = igdCmBucpeSet((uword8 *)pIgdBucpeTabTmp, sizeof(IgdBucpeTab));
	if (IGD_CM_OPERATE_SUCCESS != lRet)
	{
		CM_LOG("############ Timed Task Attribute Table Init Failed ############\n");
	}

	CM_LOG("############  Timed Task Attribute Table Init End ############\n");

	return lRet;
}

        