
#include "hi_cwmp_prmt.h"
#include "cwmp_utility.h"
#include "parameter_api.h"

#include "prmt_Bucpe.h"
/*Bucpe*/


struct CWMP_OP tBucpeLeafOPChilden= {getBucpe,setBucpe};
struct CWMP_PRMT tBucpeLeafInfo[] =
{
	{"Enable",  eCWMP_tBOOLEAN, CWMP_WRITE|CWMP_READ,  &tBucpeLeafOPChilden, (void *)&gArea_Cmcc_Common},
};
enum eBucpeLeaf
{
	eBucpeEnable,
};
struct CWMP_LEAF tBucpeLeaf[] =
{
	{&tBucpeLeafInfo[eBucpeEnable]},
	{ NULL }
};


int setBucpe(char *name, struct CWMP_LEAF *entity, int type, void *data)
{
	char *lastname = entity->info->name;
	char *buf = data;
	IgdBucpeTab stPara;
	IgdBucpeTab *pstPara = &stPara;

	if ((name == NULL) || (data == NULL) || (entity == NULL))
		return -1;
	if (entity->info->type != type)
		return ERR_9006;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdBucpeTab), 0, sizeof(IgdBucpeTab));


                    if (!strcmp(lastname, tBucpeLeafInfo[eBucpeEnable].name))
                    {
                        int *i = data;
		if (i == NULL) {
		    return ERR_9007;
		}
		if (*i < 0 || *i > 1) {
		    return ERR_9007;
		}

                        pstPara->ulBitmap = BUCPE_ATTR_MASK_BIT0_ENABLE;
                        pstPara->Enable = *(unsigned int *)buf;
                    }else
	{
		return ERR_9005;
	}

	if (pstPara->ulBitmap)
	{
		CWMP_API_SET_ENTRY_PARA_INFO_FUNC(IGD_BUCPE_TAB,
		                                  (UINT8 *)pstPara, 0, sizeof(stPara));
	}

	return 0;
}

int getBucpe(char *name, struct CWMP_LEAF *entity, int *type, void **data)
{
	char *lastname = entity->info->name;
	unsigned int msgLen = 0;
	IgdBucpeTab stPara;
	IgdBucpeTab *pstPara = &stPara;

	if ((name == NULL) || (type == NULL) || (data == NULL) || (entity == NULL))
		return -1;

	HI_OS_MEMSET_S((UINT8 *)pstPara, sizeof(IgdBucpeTab), 0, sizeof(IgdBucpeTab));

	msgLen = sizeof(stPara);
	pstPara->ulBitmap = QOS_ATTR_MASK_ALL;
	CWMP_API_GET_ENTRY_PARA_INFO_FUNC(IGD_BUCPE_TAB,
	                                  (UINT8 *)pstPara, 0, msgLen);

	*type = entity->info->type;
	*data = NULL;

	if (!strcmp(lastname, tBucpeLeafInfo[eBucpeEnable].name))
	{
		*data = booldup(pstPara->Enable);
	}
	else
	{
		return ERR_9005;
	}
	return 0;
}
       
