
#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"

#include "prmt_HgTransferQosServiceObject.h"
/*HgTransferQosServiceObject*/


struct CWMP_OP tHgTransferQosServiceObjectLeafOPChilden= {getHgTransferQosServiceObject,setHgTransferQosServiceObject};
struct CWMP_PRMT tHgTransferQosServiceObjectLeafInfo[] =
{
};
enum eHgTransferQosServiceObjectLeaf
{
};
struct CWMP_LEAF tHgTransferQosServiceObjectLeaf[] =
{
	{ NULL }
};


int setHgTransferQosServiceObject(char *name, struct CWMP_LEAF *entity, int type, void *data)
{
	char *lastname = entity->info->name;
	char *buf = data;
	IgdHgTransferQosServiceObjectTab stPara;
	IgdHgTransferQosServiceObjectTab *pstPara = &stPara;

	if ((name == NULL) || (data == NULL) || (entity == NULL))
		return -1;
	if (entity->info->type != type)
		return ERR_9006;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdHgTransferQosServiceObjectTab), 0, sizeof(IgdHgTransferQosServiceObjectTab));

else
	{
		return ERR_9005;
	}

	if (pstPara->ulBitmap)
	{
		CWMP_API_SET_ENTRY_PARA_INFO_FUNC(IGD_HGTRANSFERQOSSERVICEOBJECT_TAB,
		                                  (UINT8 *)pstPara, 0, sizeof(stPara));
	}

	return 0;
}

int getHgTransferQosServiceObject(char *name, struct CWMP_LEAF *entity, int *type, void **data)
{
	char *lastname = entity->info->name;
	unsigned int msgLen = 0;
	IgdHgTransferQosServiceObjectTab stPara;
	IgdHgTransferQosServiceObjectTab *pstPara = &stPara;

	if ((name == NULL) || (type == NULL) || (data == NULL) || (entity == NULL))
		return -1;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdHgTransferQosServiceObjectTab), 0, sizeof(IgdHgTransferQosServiceObjectTab));

	msgLen = sizeof(stPara);
	pstPara->ulBitmap = QOS_ATTR_MASK_ALL;
	CWMP_API_GET_ENTRY_PARA_INFO_FUNC(IGD_HGTRANSFERQOSSERVICEOBJECT_TAB,
	                                  (UINT8 *)pstPara, 0, msgLen);

	*type = entity->info->type;
	*data = NULL;

else
	{
		return ERR_9005;
	}
	return 0;
}
       
