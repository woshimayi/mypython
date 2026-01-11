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


word32 igdCmHgTransferQosServiceObjectGet(uword8 *pucInfo, uword32 len)
{
	word32 lRet = IGD_CM_OPERATE_SUCCESS;
	IgdHgTransferQosServiceObjectTab entry;
	IgdHgTransferQosServiceObjectTab *currObj = NULL;

	currObj = (IgdHgTransferQosServiceObjectTab *)pucInfo;
	HI_OS_MEMSET_S(&entry, sizeof(IgdHgTransferQosServiceObjectTab), 0, sizeof(IgdHgTransferQosServiceObjectTab));

	if (mib_chain_get(IGD_HGTRANSFERQOSSERVICEOBJECT_TAB, 0, (void *)&entry))
	{
		HI_OS_MEMCPY_S(currObj, sizeof(IgdHgTransferQosServiceObjectTab), &entry, sizeof(IgdHgTransferQosServiceObjectTab));
		lRet = IGD_CM_OPERATE_SUCCESS;
	}
	else
	{
		CM_LOG("mib_chain_get IGD_HGTRANSFERQOSSERVICEOBJECT_TAB is fail.\t\n");
		lRet = IGD_CM_OPERATE_FAIL;
	}

	return lRet;
}

word32 igdCmHgTransferQosServiceObjectSet(uword8 *pucInfo, uword32 len)
{
	CM_LOG("*************entry in igdCmSecureMacFilterAttrSet*************\n");

	IgdHgTransferQosServiceObjectTab currObj;
	IgdHgTransferQosServiceObjectTab *newObjTmp = NULL;

	if (!pucInfo)
		return (IGD_CM_GLOBAL_INPUT_PARA_ERROR);

	newObjTmp = (IgdHgTransferQosServiceObjectTab *)pucInfo;
	HI_OS_MEMSET_S(&currObj, sizeof(IgdHgTransferQosServiceObjectTab), 0, sizeof(IgdHgTransferQosServiceObjectTab));
	if (0 == mib_chain_get(IGD_HGTRANSFERQOSSERVICEOBJECT_TAB, 0, (void *)&currObj))
	{
		CM_LOG("mib_chain_get IGD_HGTRANSFERQOSSERVICEOBJECT_TAB is fail.\t\n");
		mib_chain_add(IGD_HGTRANSFERQOSSERVICEOBJECT_TAB, (void *)&currObj);
	}


	mib_chain_update(IGD_HGTRANSFERQOSSERVICEOBJECT_TAB, (void *)&currObj, 0);

	return 0;
}

word32 igdCmHgTransferQosServiceObjectInit(void)
{
	CM_LOG("############ Timed Task Attribute Table Init Start ############\n");

	word32 lInsNum = 0, lRet = IGD_CM_OPERATE_SUCCESS;
	IgdHgTransferQosServiceObjectTab entry;
	IgdHgTransferQosServiceObjectTab IgdHgTransferQosServiceObjectTabTmp, *pIgdHgTransferQosServiceObjectTabTmp = NULL;

	pIgdHgTransferQosServiceObjectTabTmp = &IgdHgTransferQosServiceObjectTabTmp;
	HI_OS_MEMSET_S(&entry, sizeof(IgdHgTransferQosServiceObjectTab), 0, sizeof(IgdHgTransferQosServiceObjectTab));
	HI_OS_MEMSET_S(pIgdHgTransferQosServiceObjectTabTmp, sizeof(IgdHgTransferQosServiceObjectTab), 0, sizeof(IgdHgTransferQosServiceObjectTab));

	mib_chain_get(IGD_HGTRANSFERQOSSERVICEOBJECT_TAB, lInsNum, &entry);

	HI_OS_MEMCPY_S(pIgdHgTransferQosServiceObjectTabTmp, sizeof(*pIgdHgTransferQosServiceObjectTabTmp), &entry, sizeof(IgdHgTransferQosServiceObjectTab));

	lRet = igdCmHgTransferQosServiceObjectSet((uword8 *)pIgdHgTransferQosServiceObjectTabTmp, sizeof(IgdHgTransferQosServiceObjectTab));
	if (IGD_CM_OPERATE_SUCCESS != lRet)
	{
		CM_LOG("############ Timed Task Attribute Table Init Failed ############\n");
	}

	CM_LOG("############  Timed Task Attribute Table Init End ############\n");

	return lRet;
}

        